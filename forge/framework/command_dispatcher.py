from forge.framework.command_registry import CommandRegistry
from forge.framework.command_result import CommandResult
from forge.framework.command import Command


class CommandDispatcher:

    def __init__(self, registry=None):
        self.registry = registry or CommandRegistry()

    def dispatch(self, command, context):

        if isinstance(command, str):

            command_name = command

            command = self.registry.get(command_name)

            if command is None:
                return CommandResult.fail(
                    f"Unknown command: {command_name}"
                )

        if isinstance(command, Command):
            return command.run(context)

        return command.execute(context)
