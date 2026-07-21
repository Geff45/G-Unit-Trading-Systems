from dataclasses import dataclass, field

from kernel.plugins.plugin_state import PluginState


@dataclass
class PluginDescriptor:
    """
    Metadata describing an Atlas plugin.
    """

    plugin_id: str

    name: str

    version: str

    author: str

    description: str

    service: str

    state: PluginState = PluginState.CREATED

    dependencies: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)