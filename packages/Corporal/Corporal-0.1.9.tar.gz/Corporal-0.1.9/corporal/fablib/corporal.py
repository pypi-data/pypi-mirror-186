# -*- coding: utf-8; -*-
"""
Fabric library for Corporal systems
"""

import os
import json

from rattail_fabric2 import apache, postgresql, python, exists, mkdir

from corporal.fablib import deploy_common


def bootstrap_corporal_app(c, env, envname='corporal', user='rattail',
                           port=7900, asgi=False, sitename=None, stage=False,
                           coredir=None, lanes=None,
                           core_office_url=None):
    """
    Create a virtual environment for use with a Corporal app.
    """
    safename = envname.replace('-', '_')
    dbname = envname
    if not sitename:
        sitename = envname
    envdir = '/srv/envs/{}'.format(envname)
    appdir = '{}/app'.format(envdir)
    srcdir = '{}/src'.format(envdir)
    production = not stage

    c.sudo('supervisorctl stop {}:'.format(safename), warn=True)

    # virtualenv
    if not exists(c, envdir):
        python.mkvirtualenv(c, envname, python='/usr/bin/python3', runas_user=user)
    c.sudo('chmod 0600 {}/pip.conf'.format(envdir))
    mkdir(c, srcdir, owner=user, use_sudo=True)

    # uvicorn
    if asgi:
        # (latest as of writing is 0.20.0)
        c.sudo("bash -lc 'workon {} && pip install uvicorn[standard]'".format(envname),
               user=user)

    if stage:

        # pycorepos
        if not exists(c, '{}/pycorepos'.format(srcdir)):
            c.sudo('git clone https://kallithea.rattailproject.org/rattail-project/pycorepos {}/pycorepos'.format(srcdir),
                   user=user)
            c.sudo("bash -lc 'workon {} && pip install -e {}/pycorepos'".format(envname, srcdir),
                   user=user)

        # rattail
        if not exists(c, '{}/rattail'.format(srcdir)):
            c.sudo('git clone https://kallithea.rattailproject.org/rattail-project/rattail {}/rattail'.format(srcdir),
                   user=user)
            c.sudo("bash -lc 'workon {} && pip install -e {}/rattail'".format(envname, srcdir),
                   user=user)

        # rattail-corepos
        if not exists(c, '{}/rattail-corepos'.format(srcdir)):
            c.sudo('git clone https://kallithea.rattailproject.org/rattail-project/rattail-corepos {}/rattail-corepos'.format(srcdir),
                   user=user, echo=False)
            c.sudo("bash -lc 'workon {} && pip install -e {}/rattail-corepos'".format(envname, srcdir),
                   user=user)

        # tailbone
        if not exists(c, '{}/tailbone'.format(srcdir)):
            c.sudo('git clone https://kallithea.rattailproject.org/rattail-project/tailbone {}/tailbone'.format(srcdir),
                   user=user)
            c.sudo("bash -lc 'workon {} && pip install -e {}/tailbone'".format(envname, srcdir),
                   user=user)

        # tailbone-corepos
        if not exists(c, '{}/tailbone-corepos'.format(srcdir)):
            c.sudo('git clone https://kallithea.rattailproject.org/rattail-project/tailbone-corepos {}/tailbone-corepos'.format(srcdir),
                   user=user, echo=False)
            c.sudo("bash -lc 'workon {} && pip install -e {}/tailbone-corepos'".format(envname, srcdir),
                   user=user)

        # rattail-fabric2
        if not exists(c, '{}/rattail-fabric2'.format(srcdir)):
            c.sudo('git clone https://kallithea.rattailproject.org/rattail-project/rattail-fabric2 {}/rattail-fabric2'.format(srcdir),
                   user=user)
            c.sudo("bash -lc 'workon {} && pip install -e {}/rattail-fabric2'".format(envname, srcdir),
                   user=user)

        # corporal
        if not exists(c, '{}/corporal'.format(srcdir)):
            c.sudo('git clone https://gitlab.com/ttsc/kardish/corporal.git {}/corporal'.format(srcdir),
                   user=user)
            c.sudo("bash -lc 'workon {} && pip install -e {}/corporal'".format(envname, srcdir),
                   user=user)

    else:
        c.sudo("bash -lc 'workon {} && pip install Corporal'".format(envname),
               user=user)

    # app dir
    if not exists(c, appdir):
        c.sudo("bash -lc 'workon {} && cdvirtualenv && rattail make-appdir'".format(envname), 
               user=user)
    c.sudo('chmod 0750 {}/log'.format(appdir))
    mkdir(c, '{}/data'.format(appdir), use_sudo=True, owner=user)

    # config / scripts
    deploy_common(c, 'corporal/parse-fannie-config.php', '{}/parse-fannie-config.php'.format(appdir),
                  use_sudo=True, owner=user)
    if lanes is None:
        lanes = parse_fannie_lanes(c, '{}/parse-fannie-config.php'.format(appdir), coredir)
    deploy_common(c, 'corporal/rattail.conf.mako', '{}/rattail.conf'.format(appdir),
                  use_sudo=True, owner=user, mode='0600', 
                  context={'env': env, 'envdir': envdir, 'dbname': dbname,
                           'production': production, 'lanes': lanes,
                           'core_office_url': core_office_url})
    if not exists(c, '{}/quiet.conf'.format(appdir)):
        c.sudo("bash -lc 'workon {} && cdvirtualenv app && rattail make-config -T quiet'".format(envname),
               user=user)
    deploy_common(c, 'corporal/cron.conf.mako', '{}/cron.conf'.format(appdir),
                  use_sudo=True, owner=user, context={'envdir': envdir})
    deploy_common(c, 'corporal/web.conf.mako', '{}/web.conf'.format(appdir),
                  use_sudo=True, owner=user, mode='0600', 
                  context={'env': env, 'envname': envname, 'envdir': envdir,
                           'port': port})
    if asgi:
        deploy_common(c, 'corporal/webasgi.conf.mako', '{}/webasgi.conf'.format(appdir),
                      use_sudo=True, owner=user, mode='0600',
                      context={'env': env, 'envname': envname, 'envdir': envdir})
    deploy_common(c, 'corporal/upgrade.sh.mako', '{}/upgrade.sh'.format(appdir),
                  use_sudo=True, owner=user, 
                  context={'envdir': envdir, 'production': production})
    # if host:
    deploy_common(c, 'corporal/tasks.py.mako', '{}/tasks.py'.format(appdir),
                  use_sudo=True, owner=user,
                  context={'envdir': envdir, 'stage': stage})
    deploy_common(c, 'corporal/upgrade-wrapper.sh.mako', '{}/upgrade-wrapper.sh'.format(appdir),
                  use_sudo=True, owner=user, 
                  context={'envdir': envdir, 'safename': safename})

    # database
    if not postgresql.db_exists(c, dbname):
        postgresql.create_db(c, dbname, owner='rattail', checkfirst=False)
        c.sudo("bash -lc 'workon {} && cdvirtualenv && bin/alembic -c app/rattail.conf upgrade heads'".format(envname),
               user=user)
        postgresql.sql(c, "insert into setting values ('tailbone.theme', 'falafel')",
                       database=dbname)
        postgresql.sql(c, "insert into setting values ('tailbone.themes.expose_picker', 'false')",
                       database=dbname)

    # supervisor
    deploy_common(c, 'corporal/supervisor.conf.mako', '/etc/supervisor/conf.d/{}.conf'.format(safename),
                  use_sudo=True, context={'envdir': envdir, 'safename': safename,
                                          'port': port, 'asgi': asgi})
    c.sudo('supervisorctl update')
    c.sudo('supervisorctl start {}:'.format(safename))

    # cron etc.
    deploy_common.sudoers(c, 'corporal/sudoers.mako', '/etc/sudoers.d/{}'.format(safename),
                          context={'envdir': envdir, 'safename': safename})
    deploy_common(c, 'corporal/logrotate.conf.mako', '/etc/logrotate.d/{}'.format(safename),
                  use_sudo=True, context={'envdir': envdir})

    # apache
    deploy_common.apache_site(c, 'apache/site-corporal.mako', sitename,
                              enable=True,
                              context={'sitename': sitename, 'port': port,
                                       'asgi': asgi})
    apache.restart(c)


def parse_fannie_lanes(c, script, coredir):
    """
    Parse and return the CORE lane definitions from Fannie config file.
    """
    lanes = []
    if coredir:
        config = os.path.join(coredir, 'fannie', 'config.php')
        if exists(c, config):
            result = c.run('php {} --path {} --setting FANNIE_LANES'.format(script, config),
                           hide=True)
            lanes = json.loads(result.stdout)
            for number, lane in enumerate(lanes, 1):
                lane['number'] = number
                lane['dbkey'] = 'lane{:02d}'.format(number)
    return lanes
