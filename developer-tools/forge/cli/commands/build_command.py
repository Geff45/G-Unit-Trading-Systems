from ..base.command import Command


class BuildCommand(Command):

    NAME = "build"
    DESCRIPTION = "Build the current project."

    def execute(self, args):
        print("Building project...")