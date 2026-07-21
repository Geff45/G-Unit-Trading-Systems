"""
G-UNIT Platform Kernel

Configuration Loader

Loads and manages platform configuration.
"""


import json

from pathlib import Path

from typing import Dict



class ConfigurationLoader:
    """
    Loads configuration files.
    """



    def __init__(self):

        self.configuration: Dict = {}



    def load_json(
        self,
        path: str
    ):

        file = Path(path)


        if not file.exists():

            raise FileNotFoundError(
                f"Configuration file missing: {path}"
            )


        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            self.configuration = json.load(f)


        return self.configuration



    def get(
        self,
        key: str,
        default=None
    ):

        return self.configuration.get(
            key,
            default
        )



    def all(self):

        return self.configuration