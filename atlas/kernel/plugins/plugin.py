from abc import ABC
from abc import abstractmethod

from kernel.plugins.plugin_descriptor import (
    PluginDescriptor,
)


class Plugin(ABC):
    """
    Base class for every Atlas plugin.
    """

    def __init__(
        self,
        descriptor: PluginDescriptor,
    ):

        self.descriptor = descriptor

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def unload(self):
        pass