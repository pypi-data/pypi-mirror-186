# -*- coding: utf-8; mode: html; -*-
<%inherit file="tailbone:templates/base_meta.mako" />

<%def name="footer()">
  <p class="has-text-centered">
    ${h.link_to("Corporal {}{}".format(corporal.__version__, '' if request.rattail_config.production() else '+dev'), url('about'))}
  </p>
</%def>
