"""
Atlas Database Models

Core data structures.
"""


from dataclasses import dataclass



@dataclass
class Project:


    name: str

    version: str

    owner: str



    def describe(self):

        return {

            "name": self.name,

            "version": self.version,

            "owner": self.owner

        }