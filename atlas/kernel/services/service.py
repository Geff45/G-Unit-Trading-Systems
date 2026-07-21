from abc import ABC, abstractmethod

from kernel.services.service_descriptor import (
    ServiceDescriptor,
)


class Service(ABC):

    def __init__(

        self,

        descriptor: ServiceDescriptor,

    ):

        self.descriptor = descriptor

    @abstractmethod
    def start(self):

        pass

    @abstractmethod
    def stop(self):

        pass

    @abstractmethod
    def pause(self):

        pass

    @abstractmethod
    def resume(self):

        pass