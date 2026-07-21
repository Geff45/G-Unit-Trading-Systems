from kernel.plugins.plugin_manager import (
    PluginManager,
)


class PluginLoader:
    """
    Loads Atlas plugins.
    """

    def __init__(self):

        self.manager = PluginManager()

    def load_plugins(
        self,
        plugins,
    ):

        for plugin in plugins:

            self.manager.register(plugin)

        return self.manager