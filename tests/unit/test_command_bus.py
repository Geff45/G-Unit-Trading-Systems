from gunit.commands.command import Command
from gunit.commands.command_bus import CommandBus
from gunit.commands.command_context import CommandContext
from gunit.commands.command_handler import CommandHandler
from gunit.commands.command_registry import CommandRegistry
from gunit.commands.command_result import CommandResult


class Build(Command):
    pass


class BuildHandler(CommandHandler):

    def handle(
        self,
        command,
        context,
    ):
        return CommandResult(
            True,
            "Executed",
        )


def test_dispatch():

    registry = CommandRegistry()

    registry.register(
        Build,
        BuildHandler(),
    )

    bus = CommandBus(registry)

    result = bus.dispatch(
        Build(),
        CommandContext(),
    )

    assert result.success