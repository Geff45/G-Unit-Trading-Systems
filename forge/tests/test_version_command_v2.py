from forge.commands import VersionCommand
from forge.framework import CommandContext


def test_version_command():

    command = VersionCommand()

    result = command.run(
        CommandContext()
    )

    assert result.success
    assert "Forge Version" in result.message