from abc import ABC, abstractmethod


class Extension(ABC):

    def __init__(self):
        self.context = None
        self.descriptor = None

    @abstractmethod
    def configure(self, context):
        ...

    @abstractmethod
    def enable(self):
        ...

    @abstractmethod
    def disable(self):
        ...


__all__ = ["Extension"]
