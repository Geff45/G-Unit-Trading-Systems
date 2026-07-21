"""
Atlas Intelligence
Model Registry

Maintains every AI model available inside Atlas.
"""

from typing import Dict, Optional


class ModelRegistry:

    def __init__(self):
        self._models: Dict[str, dict] = {}

    def register(self, name: str, provider: str, version: str):
        self._models[name] = {
            "provider": provider,
            "version": version,
            "loaded": False
        }

        return {
            "status": "registered",
            "model": name
        }

    def get(self, name: str) -> Optional[dict]:
        return self._models.get(name)

    def list_models(self):
        return list(self._models.keys())

    def remove(self, name: str):
        self._models.pop(name, None)

        return {
            "status": "removed",
            "model": name
        }

    def exists(self, name: str):
        return name in self._models