"""
Atlas Forge Base Service

Provides the default implementation for all Forge services.

Version: 2.0.0
"""

from __future__ import annotations

from abc import ABC

from ..interfaces import IService
from ..service_state import ServiceState


class BaseService(IService, ABC):
    """
    Base implementation of the IService interface.
    """

    SERVICE_NAME = "BaseService"
    VERSION = "2.0.0"

    def __init__(self) -> None:

        self._state = ServiceState.NEW

    @property
    def service_name(self) -> str:
        return self.SERVICE_NAME

    @property
    def version(self) -> str:
        return self.VERSION

    @property
    def state(self) -> ServiceState:
        return self._state

    def on_register(self) -> None:
        self._state = ServiceState.REGISTERED

    def initialize(self) -> None:
        self._state = ServiceState.INITIALIZING

    def start(self) -> None:
        self._state = ServiceState.RUNNING

    def stop(self) -> None:
        self._state = ServiceState.STOPPING

    def shutdown(self) -> None:
        self._state = ServiceState.STOPPED

    def fail(self) -> None:
        self._state = ServiceState.FAILED

    def health_check(self) -> bool:
        return self._state == ServiceState.RUNNING

    def __repr__(self) -> str:
        return (
            f"{self.service_name}"
            f"(version={self.version}, "
            f"state={self.state.name})"
        )