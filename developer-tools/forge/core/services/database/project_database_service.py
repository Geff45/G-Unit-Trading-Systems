"""
Atlas Forge Project Database Service

Version: 1.0.0
"""

from __future__ import annotations

from pathlib import Path

from ..base.base_service import BaseService
from .database_repository import DatabaseRepository


class ProjectDatabaseService(BaseService):
    """
    Central storage service for Atlas Forge.
    """

    SERVICE_NAME = "ProjectDatabase"

    VERSION = "1.0.0"

    def __init__(self, database_directory: Path):

        super().__init__()

        self._repository = DatabaseRepository(
            database_directory
        )

    # -------------------------------------------------
    # Project
    # -------------------------------------------------

    def load_project(self):

        return self._repository.load(
            "project.json"
        )

    def save_project(self, data):

        self._repository.save(
            "project.json",
            data
        )

    # -------------------------------------------------
    # Modules
    # -------------------------------------------------

    def load_modules(self):

        return self._repository.load(
            "modules.json"
        )

    def save_modules(self, data):

        self._repository.save(
            "modules.json",
            data
        )

    # -------------------------------------------------
    # Dependencies
    # -------------------------------------------------

    def load_dependencies(self):

        return self._repository.load(
            "dependencies.json"
        )

    def save_dependencies(self, data):

        self._repository.save(
            "dependencies.json",
            data
        )

    # -------------------------------------------------
    # Snapshots
    # -------------------------------------------------

    def load_snapshots(self):

        return self._repository.load(
            "snapshots.json"
        )

    def save_snapshots(self, data):

        self._repository.save(
            "snapshots.json",
            data
        )

    # -------------------------------------------------
    # History
    # -------------------------------------------------

    def load_history(self):

        return self._repository.load(
            "history.json"
        )

    def save_history(self, data):

        self._repository.save(
            "history.json",
            data
        )