"""
Atlas Model Manager
"""

from intelligence.model_registry import ModelRegistry


class ModelManager:

    def __init__(self):

        self.registry = ModelRegistry()

    def load_model(self, name):

        model = self.registry.get(name)

        if model:

            model["loaded"] = True

            return {
                "status": "loaded",
                "model": name
            }

        return {
            "status": "missing"
        }

    def unload_model(self, name):

        model = self.registry.get(name)

        if model:

            model["loaded"] = False

            return {
                "status": "unloaded",
                "model": name
            }

        return {
            "status": "missing"
        }

    def status(self, name):

        model = self.registry.get(name)

        if model:

            return model

        return None