from kernel.plugins.plugin_registry import (
    PluginRegistry,
)

from kernel.plugins.plugin_state import (
    PluginState,
)


class PluginManager:
    """
    Atlas Enterprise Plugin Manager.
    """

    def __init__(self):

        self.registry = PluginRegistry()

    def register(self, plugin):

        self.registry.register(plugin)

    def load(self, plugin_id):

        plugin = self.registry.get(plugin_id)

        plugin.load()

        plugin.descriptor.state = (
            PluginState.LOADED
        )

    def enable(self, plugin_id):

        plugin = self.registry.get(plugin_id)

        plugin.enable()

        plugin.descriptor.state = (
            PluginState.ENABLED
        )

    def disable(self, plugin_id):

        plugin = self.registry.get(plugin_id)

        plugin.disable()

        plugin.descriptor.state = (
            PluginState.DISABLED
        )

    def unload(self, plugin_id):

        plugin = self.registry.get(plugin_id)

        plugin.unload()

        plugin.descriptor.state = (
            PluginState.UNLOADED
        )