"""
Logging exceptions.
"""


class LoggingError(Exception):
    """Base logging exception."""


class HandlerError(LoggingError):
    """Raised when a handler fails."""


class FormatterError(LoggingError):
    """Raised when formatting fails."""