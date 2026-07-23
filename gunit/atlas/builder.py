"""
Atlas builder.
"""

from __future__ import annotations

from gunit.atlas.engine import AtlasEngine


class AtlasBuilder:
    """
    Builds AtlasEngine instances.
    """

    def build(self) -> AtlasEngine:
        return AtlasEngine()