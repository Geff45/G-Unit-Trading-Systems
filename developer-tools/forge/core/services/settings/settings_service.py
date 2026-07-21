"""
Atlas Forge Settings Service

Version: 2.0.0
"""

from pathlib import Path

from ..base import BaseService
from .settings_loader import SettingsLoader


class SettingsService(BaseService):

    SERVICE_NAME = "SettingsService"
    VERSION = "2.0.0"

    def __init__(self, settings_file: Path):

        super().__init__()

        self.settings_file = Path(settings_file)
        self.settings = None

    def initialize(self):

        super().initialize()

        self.settings = SettingsLoader.load(self.settings_file)

    def shutdown(self):

        super().shutdown()

    def get(self):
        return self.settings