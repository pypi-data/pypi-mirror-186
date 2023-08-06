# -*- coding: utf-8; -*-
"""
Static assets
"""


def includeme(config):
    config.include('tailbone.static')
    config.add_static_view('corporal', 'corporal.web:static', cache_max_age=3600)
