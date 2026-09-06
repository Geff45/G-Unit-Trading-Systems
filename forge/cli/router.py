from forge.framework.command_context import CommandContext
from forge.framework.command_dispatcher import CommandDispatcher
from forge.framework.command_registry import CommandRegistry
from forge.commands.version_command import VersionCommand
from forge.commands.doctor_command import DoctorCommand
from forge.commands.make_command import MakeCommand
from forge.commands.new_command import NewCommand


class CLIRouter:
    """
    Converts CLI arguments into command execution.
    """

    def __init__(self, registry=None):

        self.registry = registry or CommandRegistry()

        self.registry.register(
            VersionCommand()
        )

        self.registry.register(
            DoctorCommand()
        )

        self.registry.register(
            MakeCommand()
        )

        self.registry.register(
            NewCommand()
        )

        self.dispatcher = CommandDispatcher(
            self.registry
        )

    def route(self, args, context=None):

        if not args:

            from forge.framework import CommandResult

            return CommandResult.fail(
                "No command supplied"
            )

        command_name = args[0]

        command_args = args[1:]

        if context is None:
            context = CommandContext(
                command_args
            )

        return self.dispatcher.dispatch(
            command_name,
            context
        )
