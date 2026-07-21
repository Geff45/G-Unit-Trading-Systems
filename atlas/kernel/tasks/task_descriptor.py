from dataclasses import dataclass, field

from kernel.tasks.task_state import TaskState


@dataclass
class TaskDescriptor:
    """
    Enterprise task metadata.
    """

    task_id: str

    name: str

    workflow: str

    capability: str

    priority: int = 5

    timeout: int = 30

    retries: int = 3

    execution_target: str = "local"

    requires_network: bool = False

    requires_gpu: bool = False

    requires_linux: bool = False

    state: TaskState = TaskState.CREATED

    dependencies: list[str] = field(default_factory=list)