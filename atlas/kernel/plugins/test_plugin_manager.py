from kernel.plugins.plugin import Plugin

from kernel.plugins.plugin_descriptor import (
    PluginDescriptor,
)

from kernel.plugins.plugin_loader import (
    PluginLoader,
)


class TrendPlugin(Plugin):

    def load(self):

        print("Trend Plugin Loaded")

    def enable(self):

        print("Trend Plugin Enabled")

    def disable(self):

        print("Trend Plugin Disabled")

    def unload(self):

        print("Trend Plugin Unloaded")


descriptor = PluginDescriptor(
    plugin_id="trend",
    name="Trend Engine",
    version="1.0.0",
    author="Atlas",
    description="Market trend analysis",
    service="Trading Service",
)

plugin = TrendPlugin(descriptor)

loader = PluginLoader()

manager = loader.load_plugins([plugin])

print()

print("Plugins Registered:")

print(manager.registry.count())

print()

manager.load("trend")

manager.enable("trend")

print()

print(plugin.descriptor.state.value)