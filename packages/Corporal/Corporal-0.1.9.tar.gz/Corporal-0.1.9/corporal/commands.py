"""
Corporal commands
"""

import sys

from rattail import commands

from corporal import __version__


def main(*args):
    """
    Main entry point for Corporal command system
    """
    args = list(args or sys.argv[1:])
    cmd = Command()
    cmd.run(*args)


class Command(commands.Command):
    """
    Main command for Corporal
    """
    name = 'corporal'
    version = __version__
    description = "Corporal (custom Rattail system)"
    long_description = ''


class Install(commands.InstallSubcommand):
    """
    Install the Corporal app
    """
    name = 'install'
    description = __doc__.strip()

    # nb. these must be explicitly set b/c config is not available
    # when running normally, e.g. `corporal -n install`
    app_title = "Corporal"
    app_package = 'corporal'
    app_eggname = 'Corporal'
    app_pypiname = 'Corporal'
