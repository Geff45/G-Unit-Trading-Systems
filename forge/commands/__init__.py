from .make import execute as make
from .version import execute as version
from .doctor import execute as doctor

__all__ = [
    "make",
    "version",
    "doctor",
]