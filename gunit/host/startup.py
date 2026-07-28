"""
Application startup pipeline.
"""

from __future__ import annotations

from .lifetime import HostLifetime
from .service_manager import HostedServiceManager


class StartupPipeline:
    """
    Coordinates host startup and shutdown.
    """

    def __init__(
        self,
        lifetime: HostLifetime,
        services: HostedServiceManager,
    ) -> None:
        self._lifetime = lifetime
        self._services = services

    @property
    def lifetime(self) -> HostLifetime:
        return self._lifetime

    @property
    def services(self) -> HostedServiceManager:
        return self._services

    def start(self) -> None:
        self._lifetime.start()
        self._services.start_all()

    def stop(self) -> None:
        self._services.stop_all()
        self._lifetime.stop()