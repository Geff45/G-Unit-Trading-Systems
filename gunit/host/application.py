from __future__ import annotations

from gunit.di import ServiceProvider
from gunit.host.options import HostOptions
from gunit.host.environment import ApplicationEnvironment


class Application:
    """
    Application runtime context backed by the authoritative DI provider.
    """

    def __init__(
        self,
        provider: ServiceProvider,
        options: HostOptions,
    ) -> None:
        self._provider = provider
        self._options = options
        self._environment = ApplicationEnvironment(options.environment)

    @property
    def provider(self) -> ServiceProvider:
        return self._provider

    @property
    def services(self) -> ServiceProvider:
        return self._provider

    @property
    def options(self) -> HostOptions:
        return self._options

    @property
    def environment(self) -> ApplicationEnvironment:
        return self._environment
