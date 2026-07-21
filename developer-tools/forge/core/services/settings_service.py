from pathlib import Path

from .settings_loader import SettingsLoader
from .settings_model import SettingsModel


class SettingsService:
    def __init__(self, settings_file: Path | None = None):
        self.settings_file = settings_file
        self.settings: SettingsModel | None = None

    def initialize(self) -> bool:
        self.settings = SettingsLoader.load(self.settings_file)
        return True

    def shutdown(self) -> bool:
        return True

    def get_settings(self) -> SettingsModel:
        if self.settings is None:
            self.initialize()
        return self.settings