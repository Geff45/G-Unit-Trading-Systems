"""
Atlas Forge Project Database Service

Version: 2.0.0
"""

from pathlib import Path

from ..base import BaseService


class ProjectDatabaseService(BaseService):

    SERVICE_NAME = "ProjectDatabaseService"
    VERSION = "2.0.0"

    def __init__(self, database_directory: Path):

        super().__init__()

        self.database_directory = Path(database_directory)

    def initialize(self):

        super().initialize()

        self.database_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def shutdown(self):

        super().shutdown()