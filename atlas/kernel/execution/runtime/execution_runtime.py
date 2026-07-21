from abc import ABC
from abc import abstractmethod

from kernel.execution.runtime.runtime_descriptor import (
    RuntimeDescriptor,
)


class ExecutionRuntime(ABC):
    """
    Base execution runtime.

    Every runtime (Windows, Linux, WSL, GPU,
    Cloud) inherits from this class.
    """

    def __init__(
        self,
        descriptor: RuntimeDescriptor,
    ):

        self.descriptor = descriptor

    @abstractmethod
    def initialize(self):

        pass

    @abstractmethod
    def shutdown(self):

        pass

    @abstractmethod
    def execute(self, task):

        pass