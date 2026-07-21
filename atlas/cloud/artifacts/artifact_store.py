"""
Atlas Artifact Store

Handles saving and loading
Atlas artifacts.
"""


import json

from pathlib import Path



class ArtifactStore:


    def __init__(self, location="./artifacts"):

        self.location = Path(location)

        self.location.mkdir(
            parents=True,
            exist_ok=True
        )



    def save(self, artifact):

        file = (
            self.location /
            f"{artifact.name}_{artifact.version}.json"
        )


        file.write_text(
            json.dumps(
                artifact.describe(),
                indent=4
            )
        )


        return str(file)



    def list(self):

        return [

            item.name

            for item in self.location.iterdir()

            if item.is_file()

        ]