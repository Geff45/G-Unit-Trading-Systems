from forge.framework import (
    Command,
    CommandContext,
    CommandDispatcher,
    CommandResult,
)


class DemoCommand(Command):

    name = "demo"

    def execute(self, context):

        return CommandResult.ok("dispatcher")


def test_dispatcher():

    dispatcher = CommandDispatcher()

    result = dispatcher.dispatch(
        DemoCommand(),
        CommandContext(),
    )

    assert result.success
    assert result.message == "dispatcher"