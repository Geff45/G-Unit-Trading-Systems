"""
Atlas Base Engine
"""

from core.base.service import BaseService


class BaseEngine(BaseService):

    def execute(self, task):

        return {
            "engine": self.name,
            "task": task,
            "status": "completed"
        }