"""
Atlas bootstrap.
"""

from __future__ import annotations

from gunit.atlas.builder import AtlasBuilder
from gunit.atlas.engine import AtlasEngine


def bootstrap() -> AtlasEngine:
    """
    Bootstrap Atlas.
    """

    engine = AtlasBuilder().build()

    engine.boot()

    return engine