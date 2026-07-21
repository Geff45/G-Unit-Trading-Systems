"""
Atlas Base Model
"""


class BaseModel:

    def __init__(self, name, version):

        self.name = name
        self.version = version

    def info(self):

        return {
            "name": self.name,
            "version": self.version
        }