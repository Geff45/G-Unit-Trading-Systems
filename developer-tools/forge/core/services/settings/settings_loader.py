"""
Atlas Forge Settings Loader

Version: 2.0.0
"""

import json
from pathlib import Path

from .settings_model import SettingsModel


class SettingsLoader:

    @staticmethod
    def load(path: Path | None = None) -> SettingsModel:
        settings = SettingsModel()

        if path is None:
            return settings

        if not path.exists():
            return settings

        with open(path, "r", encoding="utf-8") as file:
            settings.data = json.load(file)

        return settings