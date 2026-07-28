"""
Application object.
"""

from __future__ import annotations

from gunit.container.service_container import ServiceContainer

from .environment import ApplicationEnvironment
from .options import HostOptions


class Application:
    """
    Represents a running G-Unit application.
    """

    def __init__(
        self,
        services: ServiceContainer,
        options: HostOptions,
    ) -> None:

        self._services = services
        self._options = options
        self._environment = ApplicationEnvironment(
            options.environment
        )

    @property
    def services(self) -> ServiceContainer:
        return self._services

    @property
    def options(self) -> HostOptions:
        return self._options

    @property
    def environment(self) -> ApplicationEnvironment:
        return self._environment