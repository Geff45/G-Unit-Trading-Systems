from ..base.command import Command


class CleanCommand(Command):

    NAME = "clean"
    DESCRIPTION = "Clean generated files."

    def execute(self, args):
        print("Cleaning project...")