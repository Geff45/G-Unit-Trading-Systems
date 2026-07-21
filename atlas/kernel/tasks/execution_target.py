from enum import Enum


class ExecutionTarget(Enum):
    """
    Determines where a task executes.
    """

    LOCAL = "local"

    WSL = "wsl"

    LINUX = "linux"

    CLOUD = "cloud"

    GPU = "gpu"

    AUTO = "auto"