"""
Atlas Artifact Model

Defines packages generated
by Atlas build systems.
"""


from dataclasses import dataclass, field



@dataclass
class Artifact:


    name: str

    version: str

    platform: str = "any"

    metadata: dict = field(
        default_factory=dict
    )


    def describe(self):

        return {

            "name": self.name,

            "version": self.version,

            "platform": self.platform,

            "metadata": self.metadata

        }