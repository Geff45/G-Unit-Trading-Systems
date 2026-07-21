from ..base.command import Command


class VersionCommand(Command):

    NAME = "version"

    ALIASES = [
        "ver",
        "v",
    ]

    CATEGORY = "Core"

    DESCRIPTION = "Display Forge version."

    USAGE = "forge version"

    EXAMPLES = [
        "forge version"
    ]

    def execute(self, args):

        print("Atlas Forge v2.0.0")