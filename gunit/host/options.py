"""
Host configuration options.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class HostOptions:
    """
    Configuration options for the application host.
    """

    application_name: str = "G-Unit Platform"
    environment: str = "Development"
    configuration_file: str = "config.yaml"

    enable_logging: bool = True
    enable_runtime: bool = True
    enable_scheduler: bool = True
    enable_telemetry: bool = True
    enable_plugins: bool = True

    auto_start: bool = True
    shutdown_timeout: int = 30