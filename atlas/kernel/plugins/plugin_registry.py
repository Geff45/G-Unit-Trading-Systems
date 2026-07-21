from kernel.plugins.plugin import Plugin


class PluginRegistry:
    """
    Stores all registered plugins.
    """

    def __init__(self):

        self._plugins = {}

    def register(
        self,
        plugin: Plugin,
    ):

        self._plugins[
            plugin.descriptor.plugin_id
        ] = plugin

    def get(
        self,
        plugin_id: str,
    ):

        return self._plugins.get(plugin_id)

    def exists(
        self,
        plugin_id: str,
    ):

        return plugin_id in self._plugins

    def all(self):

        return list(
            self._plugins.values()
        )

    def count(self):

        return len(
            self._plugins
        )