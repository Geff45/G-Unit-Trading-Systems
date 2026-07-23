"""
Atlas Configuration Service.
"""

from __future__ import annotations

from gunit.core.config.manager import ConfigurationManager
from gunit.core.config.schema import Configuration


class ConfigurationService:
    """
    Provides typed access to the application's configuration.
    """

    def __init__(
        self,
        manager: ConfigurationManager,
    ) -> None:
        self._manager = manager

    @property
    def configuration(self) -> Configuration:
        config = self._manager.config

        if config is None:
            raise RuntimeError(
                "Configuration has not been loaded."
            )

        return config