from enum import Enum


class WorkflowState(Enum):

    CREATED = "created"

    READY = "ready"

    RUNNING = "running"

    PAUSED = "paused"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"