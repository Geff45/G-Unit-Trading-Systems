"""
Configuration Manager.

Responsible for loading,
validating and managing
platform configuration.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .loader import ConfigurationLoader
from .validator import ConfigurationValidator
from .schema import Configuration


class ConfigurationManager:
    """
    Central configuration service.
    """

    def __init__(self) -> None:
        self._config: Configuration | None = None
        self._loaded: bool = False

        self._loader = ConfigurationLoader()
        self._validator = ConfigurationValidator()

    @property
    def config(self) -> Configuration | None:
        return self._config

    @property
    def loaded(self) -> bool:
        return self._loaded

    def load(self, path: str | Path) -> Configuration:
        raw_config = self._loader.load(path)

        self._validator.validate(raw_config)

        self._config = Configuration(**raw_config)
        self._loaded = True

        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        if self._config is None:
            return default

        return getattr(
            self._config,
            key,
            default,
        )

    def all(self) -> dict[str, Any]:
        if self._config is None:
            return {}

        return self._config.model_dump()