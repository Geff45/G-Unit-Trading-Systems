from forge.framework import Command, CommandResult


class VersionCommand(Command):

    name = "version"

    def execute(self, context):

        return CommandResult.success_result(
            "Forge Version 1.0"
        )
