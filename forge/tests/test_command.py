from forge.framework import (
    Command,
    CommandContext,
    CommandResult,
)


class DemoCommand(Command):

    name = "demo"

    def execute(self, context):

        return CommandResult.ok("executed")


def test_command():

    command = DemoCommand()

    result = command.run(
        CommandContext()
    )

    assert result.success
    assert result.message == "executed"