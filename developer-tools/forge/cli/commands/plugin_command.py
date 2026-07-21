from ..base.command import Command


class PluginCommand(Command):

    NAME = "plugin"
    DESCRIPTION = "Manage Forge plugins."

    def execute(self, args):
        print("Plugin manager...")