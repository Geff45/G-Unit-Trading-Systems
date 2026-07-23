"""
Atlas Engine.
"""

from __future__ import annotations

from gunit.atlas.context import AtlasContext
from gunit.atlas.state import AtlasState


class AtlasEngine:
    """
    Main Atlas application host.
    """

    def __init__(self) -> None:
        self._state = AtlasState.CREATED
        self._context = AtlasContext()

    @property
    def state(self) -> AtlasState:
        return self._state

    @property
    def context(self) -> AtlasContext:
        return self._context

    @property
    def running(self) -> bool:
        return self._state is AtlasState.RUNNING

    def boot(self) -> None:
        """
        Boot the Atlas engine.
        """

        self._state = AtlasState.CONFIGURING

        self._state = AtlasState.INITIALIZING

        self._state = AtlasState.STARTING

        self._state = AtlasState.RUNNING

    def shutdown(self) -> None:
        """
        Shut down Atlas.
        """

        self._state = AtlasState.STOPPING

        self._state = AtlasState.STOPPED