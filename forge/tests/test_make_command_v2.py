from pathlib import Path

from forge.commands import MakeCommand
from forge.framework import CommandContext


def test_make_usage():

    command = MakeCommand()

    result = command.run(
        CommandContext()
    )

    assert result.success is False
    assert "Usage:" in result.message


def test_make_missing_name():

    command = MakeCommand()

    result = command.run(
        CommandContext(
            args=["module"]
        )
    )

    assert result.success is False
    assert "Usage:" in result.message


def test_make_unknown_generator(tmp_path):

    command = MakeCommand()

    result = command.run(
        CommandContext(
            args=["unknown", "TestThing"],
            working_directory=str(tmp_path),
        )
    )

    assert result.success is False
    assert "Unknown generator" in result.message


def test_make_module(tmp_path):

    command = MakeCommand()

    result = command.run(
        CommandContext(
            args=["module", "TradeEngine"],
            working_directory=str(tmp_path),
        )
    )

    assert result.success is True
    assert "Generated module: TradeEngine" == result.message

    module = tmp_path / "gunit" / "modules" / "trade_engine.py"
    test = tmp_path / "tests" / "unit" / "test_trade_engine.py"

    assert module.exists()
    assert test.exists()


def test_make_module_returns_paths(tmp_path):

    command = MakeCommand()

    result = command.run(
        CommandContext(
            args=["module", "TradeEngine"],
            working_directory=str(tmp_path),
        )
    )

    assert result.success is True
    assert result.data is not None
    assert "module" in result.data
    assert "test" in result.data

    assert Path(result.data["module"]).exists()
    assert Path(result.data["test"]).exists()