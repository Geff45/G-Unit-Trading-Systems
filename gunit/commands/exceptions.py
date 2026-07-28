"""
Command exceptions.
"""


class CommandError(Exception):
    """
    Base command exception.
    """


class CommandNotFoundError(CommandError):
    """
    Raised when a command
    has no registered handler.
    """


class DuplicateCommandError(CommandError):
    """
    Raised when a command
    is registered twice.
    """