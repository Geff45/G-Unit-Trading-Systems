import pytest

from gunit.plugins import (
    Plugin,
    PluginContext,
    PluginDescriptor,
)
from gunit.plugins.plugin_registry import PluginRegistry
from gunit.di import ServiceCollection


class DemoPlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.context = None
        self.started = False
        self.stopped = False

    def configure(self, context):
        self.context = context

    def start(self):
        self.started = True

    def stop(self):
        self.stopped = True


def create_plugin(name: str):
    services = ServiceCollection()
    context = PluginContext(services)

    descriptor = PluginDescriptor(
        name=name,
        version="1.0.0",
        author="G-Unit",
        description="Demo Plugin",
    )

    plugin = DemoPlugin()

    plugin.descriptor = descriptor
    plugin.configure(context)

    return plugin


def test_register_plugin():
    registry = PluginRegistry()

    plugin = create_plugin("Demo")

    registry.register(plugin)

    assert registry.get("Demo") is plugin


def test_get_plugin():
    registry = PluginRegistry()

    plugin = create_plugin("Demo")

    registry.register(plugin)

    assert registry.get("Demo") is plugin
    assert registry.get("Unknown") is None


def test_unregister_plugin():
    registry = PluginRegistry()

    plugin = create_plugin("Demo")

    registry.register(plugin)

    registry.unregister("Demo")

    assert registry.get("Demo") is None


def test_duplicate_plugin():
    registry = PluginRegistry()

    registry.register(create_plugin("Demo"))

    with pytest.raises(ValueError):
        registry.register(create_plugin("Demo"))


def test_clear_registry():
    registry = PluginRegistry()

    registry.register(create_plugin("A"))
    registry.register(create_plugin("B"))

    registry.clear()

    assert registry.get("A") is None
    assert registry.get("B") is None