"""
Application host.
"""

from __future__ import annotations

from gunit.container.service_container import ServiceContainer

from .application import Application
from .hosted_service import HostedService
from .lifetime import HostLifetime
from .options import HostOptions
from .service_manager import HostedServiceManager
from .startup import StartupPipeline


class Host:
    """
    Main application host.
    """

    def __init__(
        self,
        services: ServiceContainer,
        options: HostOptions,
    ) -> None:

        self._application = Application(
            services=services,
            options=options,
        )

        self._lifetime = HostLifetime()

        self._service_manager = HostedServiceManager()

        self._startup = StartupPipeline(
            self._lifetime,
            self._service_manager,
        )

    @property
    def application(self) -> Application:
        return self._application

    @property
    def services(self) -> ServiceContainer:
        return self._application.services

    @property
    def options(self) -> HostOptions:
        return self._application.options

    @property
    def environment(self):
        return self._application.environment

    @property
    def lifetime(self) -> HostLifetime:
        return self._lifetime

    @property
    def hosted_services(self) -> HostedServiceManager:
        return self._service_manager

    @property
    def running(self) -> bool:
        return self._lifetime.started

    def add_service(
        self,
        service: HostedService,
    ) -> None:
        """
        Adds a hosted service.
        """

        self._service_manager.add(service)

    def remove_service(
        self,
        service: HostedService,
    ) -> None:
        """
        Removes a hosted service.
        """

        self._service_manager.remove(service)

    def clear_services(self) -> None:
        """
        Removes all hosted services.
        """

        self._service_manager.clear()

    def start(self) -> None:
        """
        Starts the application host.
        """

        self._startup.start()

    def stop(self) -> None:
        """
        Stops the application host.
        """

        self._startup.stop()

    def run(self) -> None:
        """
        Runs the application.
        """

        self.start()