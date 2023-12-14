# IntelliJ Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to intellij
INTELLIJ = 'intellij-idea-community'

# what name do you want to see in the context menu?
INTELLIJNAME = 'IntelliJ'

# always create new window?
NEWWINDOW = False


class IntelliJExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_intellij(self, menu, files):
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

        call(INTELLIJ + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='IntelliJOpen',
            label='Open in ' + INTELLIJNAME,
            tip='Opens the selected files with IntelliJ'
        )
        item.connect('activate', self.launch_intellij, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='IntelliJOpenBackground',
            label='Open in ' + INTELLIJNAME,
            tip='Opens the current directory in IntelliJ'
        )
        item.connect('activate', self.launch_intellij, [file_])

        return [item]