from abc import ABC
from abc import abstractmethod

from .plugin_context import PluginContext


class Plugin(ABC):

    @abstractmethod
    def configure(self, context: PluginContext) -> None:
        ...

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...