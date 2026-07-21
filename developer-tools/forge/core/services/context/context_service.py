"""
Atlas Forge Context Service

Version: 2.0.0
"""

from pathlib import Path

from ..base import BaseService


class ContextService(BaseService):

    SERVICE_NAME = "ContextService"
    VERSION = "2.0.0"

    def __init__(self):

        super().__init__()

        self.project_root = Path.cwd()

    @property
    def root(self):
        return self.project_root

    def initialize(self):
        super().initialize()

    def shutdown(self):
        super().shutdown()