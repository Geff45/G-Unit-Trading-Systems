"""
G-UNIT Platform Kernel

Plugin Manager

Controls loading and management
of platform extensions.
"""


from typing import Dict, Any



class PluginManager:
    """
    Manages G-UNIT plugins.
    """


    def __init__(self):

        self._plugins: Dict[str, Any] = {}



    def register(
        self,
        plugin
    ):
        """
        Register plugin.
        """

        name = plugin.name


        if name in self._plugins:

            raise Exception(
                f"Plugin already installed: {name}"
            )


        self._plugins[name] = plugin



    def load(
        self,
        name: str
    ):
        """
        Activate plugin.
        """

        plugin = self._plugins.get(name)


        if not plugin:

            raise Exception(
                f"Plugin not found: {name}"
            )


        if hasattr(
            plugin,
            "initialize"
        ):

            plugin.initialize()



        if hasattr(
            plugin,
            "activate"
        ):

            plugin.activate()



    def unload(
        self,
        name: str
    ):
        """
        Disable plugin.
        """

        plugin = self._plugins.get(name)


        if plugin and hasattr(
            plugin,
            "deactivate"
        ):

            plugin.deactivate()



    def list_plugins(
        self
    ):

        return list(
            self._plugins.keys()
        )