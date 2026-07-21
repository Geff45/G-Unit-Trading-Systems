"""
Atlas Base Component
"""

from datetime import datetime


class BaseComponent:

    def __init__(self, name):

        self.name = name
        self.created = datetime.now()
        self.status = "initialized"

    def start(self):

        self.status = "running"

        return {
            "component": self.name,
            "status": self.status
        }

    def stop(self):

        self.status = "stopped"

        return {
            "component": self.name,
            "status": self.status
        }

    def health(self):

        return {
            "component": self.name,
            "status": self.status
        }