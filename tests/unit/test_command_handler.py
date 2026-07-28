from gunit.commands import (
    Command,
    CommandContext,
    CommandResult,
)
from gunit.commands.command_handler import (
    CommandHandler,
)


class Build(Command):
    pass


class BuildHandler(CommandHandler):

    def handle(
        self,
        command,
        context,
    ):

        return CommandResult(True)


def test_handler():

    handler = BuildHandler()

    result = handler.handle(
        Build(),
        CommandContext(),
    )

    assert result.success