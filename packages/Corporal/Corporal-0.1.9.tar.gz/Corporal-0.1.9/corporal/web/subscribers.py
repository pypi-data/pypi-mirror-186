# -*- coding: utf-8; -*-
"""
Pyramid event subscribers
"""

import corporal


def add_corporal_to_context(event):
    renderer_globals = event
    renderer_globals['corporal'] = corporal


def includeme(config):
    config.include('tailbone.subscribers')
    config.add_subscriber(add_corporal_to_context, 'pyramid.events.BeforeRender')
