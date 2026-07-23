"""
Atlas application context.
"""

from __future__ import annotations

from dataclasses import dataclass

from gunit.core.config.schema import Configuration


@dataclass(slots=True)
class AtlasContext:
    """
    Shared Atlas application context.
    """

    configuration: Configuration | None = None

    logger: object | None = None

    runtime: object | None = None

    scheduler: object | None = None

    event_bus: object | None = None

    services: object | None = None