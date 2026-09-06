from forge.framework import CommandRegistry


class DummyCommand:

    name = "dummy"


def test_registry_register():

    registry = CommandRegistry()

    command = DummyCommand()

    registry.register(command)

    assert registry.exists("dummy")


def test_registry_get():

    registry = CommandRegistry()

    command = DummyCommand()

    registry.register(command)

    result = registry.get("dummy")

    assert result == command


def test_registry_remove():

    registry = CommandRegistry()

    command = DummyCommand()

    registry.register(command)

    registry.remove("dummy")

    assert registry.exists("dummy") is False


def test_registry_list():

    registry = CommandRegistry()

    registry.register(DummyCommand())

    commands = registry.list_commands()

    assert "dummy" in commands


def test_registry_exists():

    registry = CommandRegistry()

    assert registry.exists("missing") is False
