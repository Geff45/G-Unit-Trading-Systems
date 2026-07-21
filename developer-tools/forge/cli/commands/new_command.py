from ..base.command import Command


class NewCommand(Command):

    NAME = "new"
    DESCRIPTION = "Create a new Atlas project."

    def execute(self, args):
        print("Creating a new Atlas project...")