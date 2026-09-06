from pathlib import Path

from forge.commands.make_command import MakeCommand
from forge.commands.version_command import VersionCommand
from forge.commands.doctor_command import DoctorCommand
from forge.commands.new_command import NewCommand
from forge.framework import (
    Command,
    CommandContext,
    CommandDispatcher,
    CommandRegistry,
)


def test_builtin_commands_follow_command_contract():
    assert isinstance(MakeCommand(), Command)
    assert isinstance(VersionCommand(), Command)
    assert isinstance(DoctorCommand(), Command)
    assert isinstance(NewCommand(), Command)


def test_command_run_calls_validate_before_execute():

    events = []

    class LifecycleCommand(Command):
        name = "lifecycle"

        def validate(self, context):
            events.append("validate")

        def execute(self, context):
            events.append("execute")
            return "done"

    command = LifecycleCommand()

    result = command.run(CommandContext())

    assert result == "done"
    assert events == ["validate", "execute"]


def test_dispatcher_uses_command_lifecycle():

    events = []

    class LifecycleCommand(Command):
        name = "lifecycle"

        def validate(self, context):
            events.append("validate")

        def execute(self, context):
            events.append("execute")
            return "done"

    registry = CommandRegistry()
    registry.register(LifecycleCommand())

    dispatcher = CommandDispatcher(registry)

    result = dispatcher.dispatch(
        "lifecycle",
        CommandContext(),
    )

    assert result == "done"
    assert events == ["validate", "execute"]


def test_doctor_uses_context_working_directory(tmp_path):

    project_root = tmp_path / "project"
    project_root.mkdir()

    (project_root / ".git").mkdir()

    context = CommandContext(
        working_directory=str(project_root)
    )

    result = DoctorCommand().run(context)

    assert result.success is True
    assert result.data["git_repository"] is True


def test_doctor_detects_non_git_directory(tmp_path):

    project_root = tmp_path / "plain_project"
    project_root.mkdir()

    context = CommandContext(
        working_directory=str(project_root)
    )

    result = DoctorCommand().run(context)

    assert result.success is True
    assert result.data["git_repository"] is False


def test_dispatcher_keeps_legacy_execute_contract():

    class LegacyCommand:
        name = "legacy"

        def execute(self, context):
            return "legacy-result"

    registry = CommandRegistry()
    registry.register(LegacyCommand())

    dispatcher = CommandDispatcher(registry)

    result = dispatcher.dispatch(
        "legacy",
        CommandContext(),
    )

    assert result == "legacy-result"


def test_unknown_command_returns_failure():

    registry = CommandRegistry()
    dispatcher = CommandDispatcher(registry)

    result = dispatcher.dispatch(
        "does-not-exist",
        CommandContext(),
    )

    assert result.success is False
    assert "Unknown command" in result.message


def test_make_command_uses_context_working_directory(tmp_path):

    context = CommandContext(
        args=["module", "F208TestModule"],
        working_directory=str(tmp_path),
    )

    result = MakeCommand().run(context)

    assert result.success is True

    generated_file = (
        Path(tmp_path)
        / "gunit"
        / "modules"
        / "f208_test_module.py"
    )

    generated_test = (
        Path(tmp_path)
        / "tests"
        / "unit"
        / "test_f208_test_module.py"
    )

    assert generated_file.exists()
    assert generated_test.exists()
