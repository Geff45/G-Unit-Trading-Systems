from gunit.commands.command_result import CommandResult


def test_command_result():

    result = CommandResult(
        success=True,
        message="Done",
        value=123,
    )

    assert result.success

    assert result.message == "Done"

    assert result.value == 123