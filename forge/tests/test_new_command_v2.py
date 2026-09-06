from forge.commands import NewCommand
from forge.framework import CommandContext


def test_new_command(tmp_path):

    command = NewCommand()

    result = command.run(
        CommandContext(
            args=["TestProject"],
            working_directory=str(tmp_path),
        )
    )

    assert result.success is True
    assert "TestProject" in result.message