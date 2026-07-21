"""
Atlas Forge Logger Service

Version: 2.0.0
"""

from pathlib import Path

from ..base import BaseService


class LoggerService(BaseService):

    SERVICE_NAME = "LoggerService"
    VERSION = "2.0.0"

    def __init__(self, logfile: Path):

        super().__init__()

        self.logfile = Path(logfile)

    def log(self, message: str):

        print(message)

    def initialize(self):
        super().initialize()

    def shutdown(self):
        super().shutdown()