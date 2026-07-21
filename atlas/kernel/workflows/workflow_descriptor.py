from dataclasses import dataclass, field

from kernel.workflows.workflow_state import WorkflowState


@dataclass
class WorkflowDescriptor:

    workflow_id: str

    name: str

    version: str

    description: str

    priority: int = 5

    state: WorkflowState = WorkflowState.CREATED

    jobs: list = field(default_factory=list)

    dependencies: list = field(default_factory=list)