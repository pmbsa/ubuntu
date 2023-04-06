# MPS Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to MPS
MPS = 'run_scaled /home/icon0078/mps/bin/mps.sh'

# what name do you want to see in the context menu?
MPSNAME = 'MPS'

# always create new window?
NEWWINDOW = False


class MPSExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscode(self, menu, files):
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

        call(MPS + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='MPSOpen',
            label='Open in ' + MPSNAME,
            tip='Opens the selected files with MPS'
        )
        item.connect('activate', self.launch_vscode, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='MPSOpenBackground',
            label='Open in ' + MPSNAME,
            tip='Opens the current directory in MPS'
        )
        item.connect('activate', self.launch_vscode, [file_])

        return [item]
