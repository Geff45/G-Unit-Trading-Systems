from enum import Enum


class TaskState(Enum):
    """
    Enterprise task lifecycle.
    """

    CREATED = "created"

    QUEUED = "queued"

    SCHEDULED = "scheduled"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"

    RETRYING = "retrying"