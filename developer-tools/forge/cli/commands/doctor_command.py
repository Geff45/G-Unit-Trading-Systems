from ..base.command import Command


class DoctorCommand(Command):

    NAME = "doctor"

    ALIASES = [
        "doc",
        "health"
    ]

    CATEGORY = "Diagnostics"

    DESCRIPTION = "Check Forge installation."

    USAGE = "forge doctor"

    EXAMPLES = [
        "forge doctor"
    ]

    def execute(self, args):

        print("Running diagnostics...")