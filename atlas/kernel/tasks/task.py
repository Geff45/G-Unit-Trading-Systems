from abc import ABC
from abc import abstractmethod

from kernel.tasks.task_descriptor import (
    TaskDescriptor,
)

from kernel.tasks.task_result import (
    TaskResult,
)


class Task(ABC):
    """
    Base class for every Atlas task.
    """

    def __init__(
        self,
        descriptor: TaskDescriptor,
    ):

        self.descriptor = descriptor

    @abstractmethod
    def execute(self) -> TaskResult:
        pass