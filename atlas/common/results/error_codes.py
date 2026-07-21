from enum import Enum, auto


class ErrorCode(Enum):

    NONE = auto()

    VALIDATION_ERROR = auto()

    CONFIGURATION_ERROR = auto()

    STARTUP_ERROR = auto()

    SHUTDOWN_ERROR = auto()

    DEPENDENCY_ERROR = auto()

    TIMEOUT = auto()

    INTERNAL_ERROR = auto()

    UNKNOWN = auto()