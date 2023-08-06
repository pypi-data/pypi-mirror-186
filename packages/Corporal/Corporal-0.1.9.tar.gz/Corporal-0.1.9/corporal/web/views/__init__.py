# -*- coding: utf-8; -*-
"""
Corporal Views
"""


def includeme(config):

    # core views
    config.include('tailbone.views.essentials')
    config.include('tailbone.views.poser')

    # main views for CORE-POS
    config.include('tailbone_corepos.views')

    # batches
    config.include('tailbone_corepos.views.batch.vendorcatalog')
    config.include('tailbone_corepos.views.batch.coremember')
