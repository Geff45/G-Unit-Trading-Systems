"""
Application host.
"""

from __future__ import annotations

from gunit.di import ServiceProvider

from .application import Application
from .hosted_service import HostedService
from .lifetime import HostLifetime
from .options import HostOptions
from .service_manager import HostedServiceManager
from .startup import StartupPipeline


class Host:
    """
    Main application host backed by the authoritative DI provider.
    """

    def __init__(
        self,
        provider: ServiceProvider,
        options: HostOptions,
    ) -> None:

        self._provider = provider

        self._application = Application(
            provider=provider,
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
    def provider(self) -> ServiceProvider:
        return self._provider

    @property
    def services(self) -> ServiceProvider:
        return self._provider

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

    def create_scope(self):
        return self._provider.create_scope()

    def add_service(
        self,
        service: HostedService,
    ) -> None:
        """
        Adds a hosted service.
        """

        self._service_manager.add(service)

    def add_hosted_service(
        self,
        service: HostedService,
    ) -> None:
        """
        Adds a DI-resolved hosted service to the host lifecycle.
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
