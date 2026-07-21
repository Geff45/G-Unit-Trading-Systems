from abc import ABC
from abc import abstractmethod

from kernel.workflows.workflow_descriptor import (
    WorkflowDescriptor,
)


class Workflow(ABC):

    def __init__(self, descriptor: WorkflowDescriptor):

        self.descriptor = descriptor

    @abstractmethod
    def build(self):

        pass