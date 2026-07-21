from abc import ABC
from abc import abstractmethod

from kernel.capabilities.capability_descriptor import (
    CapabilityDescriptor,
)


class Capability(ABC):
    """
    Base class for every Atlas capability.
    """

    def __init__(
        self,
        descriptor: CapabilityDescriptor,
    ):

        self.descriptor = descriptor

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass