# -*- coding: utf-8; -*-
"""
Corporal web app
"""

from tailbone import app as base


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    # prefer Corporal templates over Tailbone
    settings.setdefault('mako.directories', ['corporal.web:templates',
                                             'tailbone_corepos:templates',
                                             'tailbone:templates'])

    # make config objects
    rattail_config = base.make_rattail_config(settings)
    pyramid_config = base.make_pyramid_config(settings)

    # bring in the rest of Corporal
    pyramid_config.include('corporal.web.static')
    pyramid_config.include('corporal.web.subscribers')
    pyramid_config.include('corporal.web.views')

    return pyramid_config.make_wsgi_app()


def asgi_main():
    """
    This function returns an ASGI application.
    """
    from tailbone.asgi import make_asgi_app

    return make_asgi_app(main)
