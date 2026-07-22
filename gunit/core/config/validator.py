"""
Configuration validator.
"""

from __future__ import annotations

from gunit.core.config.exceptions import ConfigurationValidationError
from gunit.core.config.schema import Configuration


class ConfigurationValidator:
    """
    Validates raw configuration dictionaries.
    """

    def validate(self, data: dict) -> Configuration:
        """
        Validate and return a strongly typed configuration.
        """
        try:
            return Configuration.model_validate(data)
        except Exception as exc:
            raise ConfigurationValidationError(str(exc)) from exc