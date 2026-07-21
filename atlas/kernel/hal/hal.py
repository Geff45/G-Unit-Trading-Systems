from abc import ABC
from abc import abstractmethod


class HardwareAbstractionLayer(ABC):
    """
    Base interface for the Atlas Hardware
    Abstraction Layer.
    """

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def collect(self):
        """
        Returns normalized hardware data.
        """
        pass