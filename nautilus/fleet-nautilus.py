# IntelliJ Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to fleet
FLEET = '/home/icon0078/.local/share/JetBrains/Toolbox/apps/fleet/bin/Fleet'

# what name do you want to see in the context menu?
FLEETNAME = 'Fleet'

# always create new window?
NEWWINDOW = False


class FleetExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_fleet(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscode
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = ''

        if NEWWINDOW:
            args = ''

        call(FLEET + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='FleetOpen',
            label='Open in ' + FLEETNAME,
            tip='Opens the selected files with Fleet'
        )
        item.connect('activate', self.launch_fleet, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='FleetOpenBackground',
            label='Open in ' + FLEETNAME,
            tip='Opens the current directory in Fleet'
        )
        item.connect('activate', self.launch_fleet, [file_])

        return [item]