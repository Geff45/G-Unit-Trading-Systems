"""
Host Builder.
"""

from __future__ import annotations

from gunit.container.service_container import ServiceContainer

from .defaults import HostDefaults
from .host import Host
from .options import HostOptions


class HostBuilder:
    """
    Builds a Host instance.
    """

    def __init__(self) -> None:

        self._services = ServiceContainer()

        self._options = HostDefaults.create()

    @property
    def services(self) -> ServiceContainer:
        return self._services

    @property
    def options(self) -> HostOptions:
        return self._options

    def use_options(
        self,
        options: HostOptions,
    ) -> "HostBuilder":

        self._options = options

        return self

    def use_defaults(self) -> "HostBuilder":

        self._options = HostDefaults.create()

        return self

    def build(self) -> Host:

        return Host(
            services=self._services,
            options=self._options,
        )