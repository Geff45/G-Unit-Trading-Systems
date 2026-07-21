"""
Atlas Forge Default Services

Version: 1.0.0
"""

from pathlib import Path

from ..services.context import ContextService
from ..services.logger import LoggerService
from ..services.settings import SettingsService
from ..services.database import ProjectDatabaseService


def create_default_services(project_root: Path):
    """
    Create all core services for Atlas Forge.
    """

    context = ContextService()

    logger = LoggerService(
        logfile=project_root / "logs" / "forge.log"
    )

    settings = SettingsService(
        settings_file=project_root / "forge.json"
    )

    database = ProjectDatabaseService(
        database_directory=project_root / "database"
    )

    return [
        context,
        logger,
        settings,
        database,
    ]