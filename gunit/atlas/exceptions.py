"""
Atlas exceptions.
"""


class AtlasError(Exception):
    """
    Base Atlas exception.
    """


class AtlasBootError(AtlasError):
    """
    Raised when Atlas fails to boot.
    """


class AtlasShutdownError(AtlasError):
    """
    Raised when Atlas fails to shut down.
    """