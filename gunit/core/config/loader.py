"""
Configuration loader.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from gunit.core.config.exceptions import (
    ConfigurationFileNotFound,
    UnsupportedConfigurationFormat,
)


class ConfigurationLoader:
    """Loads configuration files."""

    SUPPORTED = {".yaml", ".yml"}

    def load(self, path: str | Path) -> dict:
        path = Path(path)

        if not path.exists():
            raise ConfigurationFileNotFound(path)

        if path.suffix.lower() not in self.SUPPORTED:
            raise UnsupportedConfigurationFormat(path.suffix)

        with path.open("r", encoding="utf-8") as stream:
            return yaml.safe_load(stream) or {}