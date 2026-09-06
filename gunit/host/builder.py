from __future__ import annotations

from gunit.di import ServiceCollection
from gunit.host.defaults import HostDefaults
from gunit.host.host import Host
from gunit.host.options import HostOptions


class HostBuilder:
    """
    Builds a Host using the authoritative G-Unit dependency-injection system.
    """

    def __init__(self) -> None:
        self._services = ServiceCollection()
        self._options = HostDefaults.create()

    @property
    def services(self) -> ServiceCollection:
        return self._services

    @property
    def options(self) -> HostOptions:
        return self._options

    def use_defaults(self) -> HostBuilder:
        self._options = HostDefaults.create()
        return self

    def use_options(self, options: HostOptions) -> HostBuilder:
        self._options = options
        return self

    def build(self) -> Host:
        provider = self._services.build_provider()
        return Host(
            provider=provider,
            options=self._options,
        )
