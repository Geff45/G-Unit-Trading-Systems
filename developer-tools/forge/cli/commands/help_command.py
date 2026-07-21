from ..base.command import Command


class HelpCommand(Command):

    NAME = "help"
    ALIASES = ["h", "?"]

    CATEGORY = "Core"

    DESCRIPTION = "Display Forge help."

    USAGE = "forge help"

    EXAMPLES = [
        "forge help",
        "forge doctor",
        "forge version",
    ]

    def execute(self, args):

        print("\nAtlas Forge Help\n")