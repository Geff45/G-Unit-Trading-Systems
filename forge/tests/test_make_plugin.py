from pathlib import Path

from forge.commands import MakeCommand
from forge.framework import CommandContext


def test_make_plugin(tmp_path):

    command = MakeCommand()

    result = command.run(
        CommandContext(
            args=["plugin", "market_plugin"],
            working_directory=str(tmp_path),
        )
    )

    assert result.success is True
    assert result.message == "Generated plugin: market_plugin"

    plugin = (
        tmp_path
        / "plugins"
        / "market_plugin.py"
    )

    assert plugin.exists()
    assert plugin.is_file()


def test_make_plugin_returns_path(tmp_path):

    command = MakeCommand()

    result = command.run(
        CommandContext(
            args=["plugin", "market_plugin"],
            working_directory=str(tmp_path),
        )
    )

    assert result.success is True
    assert isinstance(
        result.data,
        Path,
    )

    assert result.data.exists()
