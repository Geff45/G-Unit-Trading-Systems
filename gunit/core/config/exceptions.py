"""
Configuration exceptions for the G-UNIT Platform.
"""

from __future__ import annotations


class ConfigurationError(Exception):
    """Base class for configuration-related errors."""


class ConfigurationFileNotFound(ConfigurationError):
    """Raised when a configuration file cannot be located."""


class ConfigurationValidationError(ConfigurationError):
    """Raised when configuration validation fails."""


class UnsupportedConfigurationFormat(ConfigurationError):
    """Raised when a configuration format is unsupported."""