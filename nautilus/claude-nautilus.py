# Claude Code Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to claude
CLAUDE = '/home/icon0078/.local/bin/claude'

# what name do you want to see in the context menu?
CLAUDENAME = 'Claude Code'

# terminal emulator
TERMINAL = 'gnome-terminal'


class ClaudeCodeExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_claude(self, menu, files):
        for file in files:
            filepath = file.get_location().get_path()

            if os.path.isdir(filepath) and os.path.exists(filepath):
                dirpath = filepath
            elif os.path.exists(filepath):
                dirpath = os.path.dirname(filepath)
            else:
                continue

            call(TERMINAL + ' -- bash -c \'cd "' + dirpath + '" && ' + CLAUDE + '\' &', shell=True)
            break

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='ClaudeCodeOpen',
            label='Open in ' + CLAUDENAME,
            tip='Opens the selected folder in Claude Code'
        )
        item.connect('activate', self.launch_claude, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='ClaudeCodeOpenBackground',
            label='Open in ' + CLAUDENAME,
            tip='Opens the current directory in Claude Code'
        )
        item.connect('activate', self.launch_claude, [file_])

        return [item]
