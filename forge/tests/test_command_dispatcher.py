from forge.framework import CommandDispatcher


def test_unknown_command_preserves_name():

    dispatcher = CommandDispatcher()

    result = dispatcher.dispatch(
        "banana",
        {},
    )

    assert result.success is False
    assert result.message == "Unknown command: banana"