from gunit.commands.command import Command
from gunit.commands.dispatcher import CommandDispatcher
from gunit.commands.handler import CommandHandler
from gunit.commands.registry import CommandRegistry
from gunit.commands.result import CommandResult


class Ping(Command):
    pass


class PingHandler(CommandHandler):

    def handle(
        self,
        command: Command,
    ) -> CommandResult:

        return CommandResult(
            success=True,
            value="pong",
        )


def test_dispatcher():

    registry = CommandRegistry()

    registry.register(
        Ping,
        PingHandler(),
    )

    dispatcher = CommandDispatcher(
        registry
    )

    result = dispatcher.dispatch(
        Ping()
    )

    assert result.success

    assert result.value == "pong"