from gunit.commands.command import Command
from gunit.commands.command_handler import CommandHandler
from gunit.commands.command_registry import CommandRegistry
from gunit.commands.command_result import CommandResult
from gunit.commands.command_context import CommandContext


class Build(Command):
    pass


class BuildHandler(CommandHandler):

    def handle(
        self,
        command,
        context,
    ):
        return CommandResult(True)


def test_registry():

    registry = CommandRegistry()

    registry.register(
        Build,
        BuildHandler(),
    )

    assert registry.contains(Build)