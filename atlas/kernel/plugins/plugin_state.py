from enum import Enum


class PluginState(Enum):
    """
    Enterprise plugin lifecycle.
    """

    CREATED = "created"

    LOADING = "loading"

    LOADED = "loaded"

    ENABLED = "enabled"

    DISABLED = "disabled"

    FAILED = "failed"

    UNLOADED = "unloaded"