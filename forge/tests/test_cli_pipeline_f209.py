from pathlib import Path

from forge.cli import CLIRouter
from forge.framework import (
    Command,
    CommandContext,
    CommandDispatcher,
    CommandRegistry,
    CommandResult,
)


class CaptureCommand(Command):

    name = "capture"

    def execute(self, context):

        return CommandResult.ok(
            "context captured",
            {
                "args": context.args,
                "options": context.options,
                "working_directory": context.working_directory,
            },
        )


def create_router(command=None):

    registry = CommandRegistry()

    if command is None:
        command = CaptureCommand()

    registry.register(command)

    return CLIRouter(registry)


def test_cli_router_creates_context_when_none_is_supplied():

    router = create_router()

    result = router.route(
        ["capture", "alpha", "beta"]
    )

    assert result.success is True
    assert result.data["args"] == ["alpha", "beta"]


def test_cli_router_preserves_supplied_context():

    router = create_router()

    context = CommandContext(
        args=["original"],
        options={"mode": "test"},
        working_directory="C:\\F209Project",
    )

    result = router.route(
        ["capture"],
        context,
    )

    assert result.success is True
    assert result.data["args"] == ["original"]
    assert result.data["options"] == {"mode": "test"}
    assert result.data["working_directory"] == "C:\\F209Project"


def test_cli_context_reaches_dispatcher():

    captured = {}

    class CaptureCommand(Command):

        name = "capture"

        def execute(self, context):
            captured["context"] = context

            return CommandResult.ok(
                "captured"
            )

    registry = CommandRegistry()
    registry.register(CaptureCommand())

    dispatcher = CommandDispatcher(registry)

    context = CommandContext(
        args=["one", "two"],
        options={"environment": "test"},
        working_directory="C:\\F209",
    )

    result = dispatcher.dispatch(
        "capture",
        context,
    )

    assert result.success is True
    assert captured["context"] is context


def test_router_dispatcher_command_lifecycle():

    events = []

    class LifecycleCommand(Command):

        name = "lifecycle"

        def validate(self, context):
            events.append("validate")

        def execute(self, context):
            events.append("execute")

            return CommandResult.ok(
                "complete"
            )

    registry = CommandRegistry()
    registry.register(LifecycleCommand())

    router = CLIRouter(registry)

    context = CommandContext(
        args=["value"],
        options={"test": "true"},
        working_directory="C:\\F209",
    )

    result = router.route(
        ["lifecycle"],
        context,
    )

    assert result.success is True
    assert events == [
        "validate",
        "execute",
    ]


def test_router_handles_empty_arguments():

    router = create_router()

    result = router.route([])

    assert result.success is False
    assert "No command supplied" in result.message


def test_router_handles_unknown_command():

    registry = CommandRegistry()
    router = CLIRouter(registry)

    result = router.route(
        ["does-not-exist"]
    )

    assert result.success is False
    assert "Unknown command" in result.message


def test_make_command_real_cli_output(tmp_path):

    from forge.commands.make_command import MakeCommand

    registry = CommandRegistry()
    registry.register(MakeCommand())

    router = CLIRouter(registry)

    context = CommandContext(
        args=["plugin", "f209_pipeline_plugin"],
        working_directory=str(tmp_path),
    )

    result = router.route(
        ["make"],
        context,
    )

    assert result.success is True

    generated = (
        Path(tmp_path)
        / "plugins"
        / "f209_pipeline_plugin.py"
    )

    assert generated.exists()


def test_version_command_reaches_cli_pipeline():

    from forge.commands.version_command import VersionCommand

    registry = CommandRegistry()
    registry.register(VersionCommand())

    router = CLIRouter(registry)

    result = router.route(
        ["version"]
    )

    assert result.success is True
    assert result.message == "Forge Version 1.0"
