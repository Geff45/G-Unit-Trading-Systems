"""
Atlas AI Operating System
=========================

Module:
    BaseService

Purpose:
    Provides the default implementation shared by all Atlas services.

Author:
    Atlas Development Team

Version:
    1.0.0
"""

from __future__ import annotations

from abc import ABC
from datetime import datetime
from typing import Any, Dict

from common.interfaces.i_service import IService


class BaseService(IService, ABC):
    """
    Base implementation of every Atlas service.
    """

    def __init__(self, name: str, version: str = "1.0.0") -> None:

        self._name = name
        self._version = version

        self._initialized = False
        self._configured = False
        self._running = False

        self._configuration: Dict[str, Any] = {}

        self._started_at: datetime | None = None

    # ---------------------------------------------------
    # Lifecycle
    # ---------------------------------------------------

    def initialize(self) -> None:
        self._initialized = True

    def configure(self, configuration: Dict[str, Any]) -> None:
        self._configuration.update(configuration)
        self._configured = True

    def validate(self) -> bool:
        return self._initialized

    def start(self) -> None:

        if not self.validate():
            raise RuntimeError(
                f"{self._name} failed validation."
            )

        self._running = True
        self._started_at = datetime.utcnow()

    def pause(self) -> None:
        self._running = False

    def resume(self) -> None:
        self._running = True

    def stop(self) -> None:
        self._running = False

    def shutdown(self) -> None:

        self.stop()

        self._initialized = False
        self._configured = False

    # ---------------------------------------------------
    # Monitoring
    # ---------------------------------------------------

    def health(self) -> Dict[str, Any]:

        return {

            "service": self._name,

            "healthy": self._initialized,

            "running": self._running,

            "configured": self._configured
        }

    def metrics(self) -> Dict[str, Any]:

        uptime = None

        if self._started_at:

            uptime = (
                datetime.utcnow() -
                self._started_at
            ).total_seconds()

        return {

            "uptime_seconds": uptime,

            "running": self._running
        }

    # ---------------------------------------------------
    # Information
    # ---------------------------------------------------

    def version(self) -> str:
        return self._version

    def information(self) -> Dict[str, Any]:

        return {

            "name": self._name,

            "version": self._version,

            "initialized": self._initialized,

            "configured": self._configured,

            "running": self._running
        }