from ..base.command import Command


class InstallCommand(Command):

    NAME = "install"
    DESCRIPTION = "Install project dependencies."

    def execute(self, args):
        print("Installing dependencies...")