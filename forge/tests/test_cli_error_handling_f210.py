import subprocess
import sys

from forge.cli.main import main
from forge.framework import CommandResult


def run_cli(*args):
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "forge",
            *args,
        ],
        capture_output=True,
        text=True,
    )


def test_main_no_arguments_returns_zero():
    assert main([]) == 0


def test_main_help_returns_zero():
    assert main(["--help"]) == 0
    assert main(["-h"]) == 0


def test_main_version_returns_zero():
    assert main(["--version"]) == 0


def test_unknown_command_returns_nonzero():
    result = run_cli("does-not-exist")

    assert result.returncode != 0
    assert "Unknown command" in result.stdout


def test_missing_make_arguments_returns_nonzero():
    result = run_cli("make")

    assert result.returncode != 0
    assert "Usage: forge make <type> <name>" in result.stdout


def test_invalid_generator_type_returns_nonzero():
    result = run_cli(
        "make",
        "not-a-real-generator",
        "ExampleThing",
    )

    assert result.returncode != 0
    assert "Unknown generator:" in result.stdout


def test_invalid_name_returns_nonzero():
    result = run_cli(
        "make",
        "module",
        "123-invalid",
    )

    assert result.returncode != 0


def test_successful_version_command_returns_zero():
    result = run_cli("version")

    assert result.returncode == 0
    assert "Forge Version 1.0" in result.stdout


def test_successful_doctor_command_returns_zero():
    result = run_cli("doctor")

    assert result.returncode == 0
    assert "Forge system healthy" in result.stdout


def test_command_result_failure_maps_to_nonzero(monkeypatch):

    import importlib

    cli_main_module = importlib.import_module(
        "forge.cli.main"
    )

    class FakeRouter:

        def route(self, args, context):
            return CommandResult.fail(
                "Intentional F-210 failure"
            )

    monkeypatch.setattr(
        cli_main_module,
        "CLIRouter",
        lambda registry: FakeRouter(),
    )

    exit_code = cli_main_module.main(
        ["version"]
    )

    assert exit_code == 1


def test_failed_cli_command_has_no_traceback():
    result = run_cli(
        "make",
        "not-a-real-generator",
        "ExampleThing",
    )

    combined = result.stdout + result.stderr

    assert result.returncode != 0
    assert "Traceback (most recent call last)" not in combined


def test_unknown_command_has_no_traceback():
    result = run_cli(
        "does-not-exist"
    )

    combined = result.stdout + result.stderr

    assert result.returncode != 0
    assert "Traceback (most recent call last)" not in combined
