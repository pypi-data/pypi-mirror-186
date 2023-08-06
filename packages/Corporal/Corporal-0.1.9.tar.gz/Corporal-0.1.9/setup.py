# -*- coding: utf-8; -*-
"""
Corporal setup script
"""

import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'corporal', '_version.py')).read())
README = open(os.path.join(here, 'README.md')).read()


requires = [
    #
    # Version numbers within comments below have specific meanings.
    # Basically the 'low' value is a "soft low," and 'high' a "soft high."
    # In other words:
    #
    # If either a 'low' or 'high' value exists, the primary point to be
    # made about the value is that it represents the most current (stable)
    # version available for the package (assuming typical public access
    # methods) whenever this project was started and/or documented.
    # Therefore:
    #
    # If a 'low' version is present, you should know that attempts to use
    # versions of the package significantly older than the 'low' version
    # may not yield happy results.  (A "hard" high limit may or may not be
    # indicated by a true version requirement.)
    #
    # Similarly, if a 'high' version is present, and especially if this
    # project has laid dormant for a while, you may need to refactor a bit
    # when attempting to support a more recent version of the package.  (A
    # "hard" low limit should be indicated by a true version requirement
    # when a 'high' version is present.)
    #
    # In any case, developers and other users are encouraged to play
    # outside the lines with regard to these soft limits.  If bugs are
    # encountered then they should be filed as such.
    #
    # package                           # low                   high

    # TODO: relax this once changes are dealt with upstream
    'pyramid<2',

    # NOTE: we do not specify a restriction here, but in practice you may
    # need to explicitly install e.g. 8.0.17 depending on how it behaves...
    'mysql-connector-python',

    # TODO: this is the same restriction as upstream (rattail) uses.
    # at first i didn't set this here, but for some reason an install
    # got SA 1.4.x so then i had to.
    'SQLAlchemy<1.4',                   # 0.7.6                 1.3.24

    'invoke',                           # 1.4.1
    'psycopg2',                         # 2.8.4

    'rattail[db,bouncer]',              # 0.9.141
    'rattail-fabric2',                  # 0.2.1
    'Tailbone',                         # 0.8.72
    'pyCOREPOS',                        # 0.1.1
    'rattail-corepos',                  # 0.1.3
    'tailbone-corepos',                 # 0.1.3
]


setup(
    name = "Corporal",
    version = __version__,
    author = "Lance Edgar",
    author_email = "lance@edbob.org",
    url = "https://rattailproject.org",
    description = "Companion Back-end for CORE-POS",
    long_description = README,

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business',
    ],

    install_requires = requires,
    packages = find_packages(),
    include_package_data = True,
    # zip_safe = False,

    entry_points = {

        'console_scripts': [
            'corporal = corporal.commands:main',
        ],

        'corporal.commands': [
            'install = corporal.commands:Install',
        ],

        'paste.app_factory': [
            'main = corporal.web.app:main',
        ],

        'rattail.config.extensions': [
            'corporal = corporal.config:CorporalConfig',
        ],

        'rattail.emails': [
            'corporal = corporal.emails',
        ],
    },
)
