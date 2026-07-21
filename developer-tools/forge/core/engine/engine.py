"""
Atlas Forge Engine

Central application engine.

Version: 2.0.0
"""

from __future__ import annotations

from .engine_state import EngineState
from .engine_report import EngineReport

from ..services.manager import ServiceManager


class AtlasEngine:

    VERSION = "2.0.0"

    def __init__(self):

        self._state = EngineState.CREATED

        self._services = ServiceManager()

    @property
    def services(self):

        return self._services

    @property
    def state(self):

        return self._state

    def initialize(self):

        self._state = EngineState.INITIALIZING

        self._services.initialize_all()

    def start(self):

        self._services.start_all()

        self._state = EngineState.RUNNING

    def stop(self):

        self._state = EngineState.STOPPING

        self._services.stop_all()

    def shutdown(self):

        self._services.shutdown_all()

        self._state = EngineState.STOPPED

    def report(self):

        running = 0
        failed = 0

        for service_name in self._services.list_services():

            service = self._services.get(service_name)

            if service.health_check():
                running += 1
            else:
                failed += 1

        return EngineReport(
            state=self._state.name,
            version=self.VERSION,
            registered_services=self._services.count(),
            running_services=running,
            failed_services=failed,
        )