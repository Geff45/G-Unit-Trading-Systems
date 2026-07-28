from gunit.commands.command_context import CommandContext


def test_context_defaults():

    context = CommandContext()

    assert context.user is None

    assert context.metadata == {}