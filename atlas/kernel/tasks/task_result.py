from dataclasses import dataclass


@dataclass
class TaskResult:
    """
    Standard task execution result.
    """

    success: bool

    message: str

    data: object = None

    execution_time: float = 0.0