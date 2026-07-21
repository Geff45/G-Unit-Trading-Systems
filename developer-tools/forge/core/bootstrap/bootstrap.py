"""
Atlas Forge Bootstrap

Version: 2.0.0
"""

from pathlib import Path

# Import directly from engine.py
from ..engine.engine import AtlasEngine

from .default_services import create_default_services


class Bootstrap:
    """
    Creates and configures the Atlas Engine.
    """

    def __init__(self) -> None:

        self.project_root = Path.cwd()

    def create_engine(self) -> AtlasEngine:

        engine = AtlasEngine()

        services = create_default_services(
            self.project_root
        )

        for service in services:
            engine.services.register(service)

        return engine