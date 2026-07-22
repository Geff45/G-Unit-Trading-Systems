"""
Configuration Manager.

Responsible for loading,
validating and managing
platform configuration.
"""

from __future__ import annotations

from pathlib import Path

from .loader import ConfigurationLoader
from .validator import ConfigurationValidator
from .schema import Configuration


class ConfigurationManager:
    """
    Central configuration service.
    """

    def __init__(self):

        self._config = None

        self._loaded = False

        self._loader = ConfigurationLoader()

        self._validator = ConfigurationValidator()


    @property
    def config(self):

        return self._config


    @property
    def loaded(self):

        return self._loaded


    def load(self, path: str | Path):

        raw_config = self._loader.load(path)

        self._validator.validate(raw_config)

        self._config = Configuration(
            **raw_config
        )

        self._loaded = True

        return self._config


    def get(self, key: str, default=None):

        if not self._config:
            return default

        return getattr(
            self._config,
            key,
            default
        )


    def all(self):

        if not self._config:
            return {}

        return self._config.model_dump()