from pathlib import Path
import yaml


class ConfigLoader:

    def load(self, filename: str):

        path = Path("configs") / filename

        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)