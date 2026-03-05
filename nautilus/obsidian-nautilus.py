# Obsidian Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# Opens folders as Obsidian vaults.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

OBSIDIAN = 'obsidian'
OBSIDIANNAME = 'Obsidian'


class ObsidianExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_obsidian(self, menu, files):
        for file in files:
            filepath = file.get_location().get_path()
            if os.path.isdir(filepath) and os.path.exists(filepath):
                call(OBSIDIAN + ' "' + filepath + '" &', shell=True)

    def get_file_items(self, *args):
        files = args[-1]

        # Only show for directories
        if not all(f.is_directory() for f in files):
            return []

        item = Nautilus.MenuItem(
            name='ObsidianOpen',
            label='Open in ' + OBSIDIANNAME,
            tip='Opens the selected folder as an Obsidian vault'
        )
        item.connect('activate', self.launch_obsidian, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='ObsidianOpenBackground',
            label='Open in ' + OBSIDIANNAME,
            tip='Opens the current directory as an Obsidian vault'
        )
        item.connect('activate', self.launch_obsidian, [file_])

        return [item]
