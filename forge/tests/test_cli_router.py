from forge.cli import CLIRouter
from forge.framework import CommandRegistry, CommandContext


class DummyCommand:

    name = "hello"

    def execute(self, context):

        return "executed"


class ContextCommand:

    name = "context"

    def execute(self, context):

        return context


def test_router():

    registry = CommandRegistry()

    registry.register(
        DummyCommand()
    )

    router = CLIRouter(
        registry
    )

    result = router.route(
        ["hello"],
        {}
    )

    assert result == "executed"


def test_router_preserves_context():

    registry = CommandRegistry()

    registry.register(
        ContextCommand()
    )

    router = CLIRouter(
        registry
    )

    context = CommandContext(
        args=["original"],
        options={"test": "value"},
        working_directory="C:\\test-project",
    )

    result = router.route(
        ["context"],
        context
    )

    assert result is context
    assert result.args == ["original"]
    assert result.options == {"test": "value"}
    assert result.working_directory == "C:\\test-project"
