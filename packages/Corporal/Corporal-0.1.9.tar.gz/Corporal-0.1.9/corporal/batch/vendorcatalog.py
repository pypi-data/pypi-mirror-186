# -*- coding: utf-8; -*-
"""
Handler for Vendor Catalog batches
"""

import decimal

from sqlalchemy import orm

from corepos.db.office_op import Session as CoreSession, model as corepos

from rattail_corepos.corepos.api import make_corepos_api
from rattail_corepos.batch import vendorcatalog as base


class VendorCatalogHandler(base.VendorCatalogHandler):
    """
    Handler for vendor catalog batches.
    """
    # upstream logic requires versioning hacks, but we do not
    populate_with_versioning = True
    refresh_with_versioning = True
    execute_with_versioning = True

    # catalog parsers will favor case cost, but CORE favors unit cost.  so we
    # always "ignore" unit cost diffs less than one penny to avoid useless
    # updates caused by simple rounding
    unit_cost_diff_threshold = decimal.Decimal('0.01')

    def setup_common(self, batch, progress=None):
        self.core_session = CoreSession()

        query = self.core_session.query(corepos.Product)\
                                 .options(orm.joinedload(corepos.Product.vendor_items))
        self.core_products_by_upc = self.cache_model(self.core_session,
                                                     corepos.Product,
                                                     key='upc',
                                                     query=query,
                                                     progress=progress)

        query = self.core_session.query(corepos.VendorItem)\
                                 .filter(corepos.VendorItem.vendor_id == int(batch.vendor_id))
        self.core_vendor_items_by_sku = self.cache_model(self.core_session,
                                                         corepos.VendorItem,
                                                         key='sku',
                                                         query=query,
                                                         progress=progress)
        self.core_vendor_items_by_upc = self.cache_model(self.core_session,
                                                         corepos.VendorItem,
                                                         key='upc',
                                                         query=query,
                                                         progress=progress)

    setup_populate = setup_common
    setup_refresh = setup_common

    def teardown_common(self, batch, progress=None):
        self.core_session.rollback()
        self.core_session.close()
        del self.core_session

    teardown_populate = teardown_common
    teardown_refresh = teardown_common

    def add_row(self, batch, row):

        # parser logic sets upc but we want to use item_id
        row.item_id = str(row.upc)[:-1]

        # okay now continue as normal
        # (note, this must come last b/c it will refresh row)
        super(VendorCatalogHandler, self).add_row(batch, row)

    def refresh_row(self, row):

        # clear this first in case it's set
        row.status_text = None

        # find the CORE `products` record, matching by `products.upc`
        core_product = self.core_products_by_upc.get(row.item_id)

        # find the CORE `vendorItems` record, matching by `vendorItems.sku`
        # preferably, but falling back to match on `vendorItems.upc`
        core_vendor_item = self.core_vendor_items_by_sku.get(row.vendor_code)
        if not core_vendor_item:
            core_vendor_item = self.core_vendor_items_by_upc.get(row.item_id)

        # if the catalog UPC is not found in `products` but the SKU *is* found
        # in `vendorItems` *and* the latter ties back to valid `products`
        # record, then we want to pretend that matched all along.  and not just
        # for the moment, but going forward; so we also update `row.item_id`
        if not core_product and core_vendor_item:
            core_product = core_vendor_item.product
            if core_product:
                row.item_id = core_product.upc

        # figure out if this vendor is already default for the product.  if the
        # product does not yet have a default, let this vendor be it.
        row.is_preferred_vendor = False
        row.make_preferred_vendor = False
        if core_product:
            if core_product.default_vendor_id and (
                    str(core_product.default_vendor_id) == row.batch.vendor_id):
                row.is_preferred_vendor = True
            if not core_product.default_vendor_id:
                row.make_preferred_vendor = True

        # declare "product not found" if we did not find any matches in CORE
        if not core_vendor_item and not core_product:
            row.status_code = row.STATUS_PRODUCT_NOT_FOUND
            return

        # declare "new cost" if we found `products` match but not `vendorItems`
        if not core_vendor_item:
            row.status_code = row.STATUS_NEW_COST
            return

        # declare "change product" if `vendorItems.upc` != `products.upc`
        if core_vendor_item.upc != row.item_id:
            row.status_code = row.STATUS_CHANGE_PRODUCT
            row.status_text = "new UPC {} differs from old UPC {}".format(
                row.item_id, core_vendor_item.upc)
            return

        # declare "old" `vendorItems` data
        row.old_vendor_code = core_vendor_item.sku
        row.old_case_size = core_vendor_item.units
        row.old_unit_cost = core_vendor_item.cost
        if core_vendor_item.cost is None:
            row.old_case_cost = None
        else:
            row.old_case_cost = (core_vendor_item.cost * decimal.Decimal(core_vendor_item.units))\
               .quantize(decimal.Decimal('0.12345'))

        self.refresh_cost_diffs(row)
        self.set_status_per_diffs(row)

    def describe_execution(self, batch, **kwargs):
        return ("The `vendorItems` table in CORE-POS will be updated directly "
                "via API, for all rows indicating a change etc.  In some cases "
                "`products` may also be updated as appropriate.")

    def execute(self, batch, progress=None, **kwargs):
        """
        Update CORE-POS etc.
        """
        rows = [row for row in batch.active_rows()
                if row.status_code in (row.STATUS_NEW_COST,
                                       # row.STATUS_UPDATE_COST,
                                       # row.STATUS_CHANGE_VENDOR_ITEM_CODE,
                                       row.STATUS_CHANGE_CASE_SIZE,
                                       row.STATUS_CHANGE_COST,
                                       row.STATUS_CHANGE_PRODUCT)]

        if rows:
            self.api = make_corepos_api(self.config)
            self.update_corepos(batch, rows, batch.vendor_id, progress=progress,
                                # update_product_costs=kwargs.get('update_product_costs', False),
            )

        return True

    def update_corepos(self, batch, rows, vendor_id, progress=None,
                       # TODO: this kwarg seems perhaps useful, but for now we
                       # are auto-detecting when such an update is needed
                       #update_product_costs=False,
    ):
        """
        Update the `vendorItems` table in CORE-POS (and maybe `products` too).
        """

        def update(row, i):
            # we may need this value in a couple places
            unit_cost = float(row.unit_cost)

            # figure out if we are "updating the same, primary" cost record,
            # b/c if so we will want to update product accordingly also.  this
            # is always the case when this is the first vendor for product.
            # updating_primary = first_vendor
            updating_primary = row.make_preferred_vendor
            if not updating_primary:
                core_vendor_items = self.api.get_vendor_items(upc=row.item_id)
                if core_vendor_items:
                    core_vendor_item = core_vendor_items[0]
                    if core_vendor_item['sku'] == row.vendor_code:
                        updating_primary = True

            # create or update the `vendorItems` record in CORE
            self.api.set_vendor_item(sku=row.vendor_code,
                                     vendorID=vendor_id,
                                     upc=row.item_id,
                                     brand=row.brand_name,
                                     description=row.description,
                                     size=row.size,
                                     units=row.case_size,
                                     cost=unit_cost,
                                     # TODO: we (may) have vendor SRP, but pretty
                                     # sure CORE has different plans for its `srp`
                                     #srp=row.suggested_retail,
            )

            # TODO: CORE does not have the concept of a true "default"
            # `vendorItems` record, but rather uses the `modified` timestamp
            # for pseudo-default.  this means any given product may wind up
            # with a new/different pseudo-default when the above operation
            # completes.  in which case, perhaps we should *always* update
            # `products.cost` accordingly (below)..?  er, still only if the
            # product's `default_vendor_id` matches at least, i guess...  for
            # now we are only doing so if it "obviously" needs it.

            # maybe also update `products` record in CORE
            kwargs = {}
            if updating_primary:
                kwargs['cost'] = unit_cost
            if row.make_preferred_vendor:
                kwargs['default_vendor_id'] = vendor_id
            if kwargs:
                self.api.set_product(upc=row.item_id, **kwargs)

        self.progress_loop(update, rows, progress,
                           message="Updating CORE-POS via API")
