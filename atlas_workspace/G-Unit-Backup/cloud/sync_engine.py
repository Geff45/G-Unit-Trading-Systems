"""
Atlas Sync Engine

Handles project synchronization
between local and cloud workspaces.
"""


from pathlib import Path
import shutil



class SyncEngine:


    def push(self, source, destination):

        source = Path(source)

        destination = Path(destination)


        if not source.exists():

            return {
                "status":"error",
                "message":"source_not_found"
            }


        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True
        )


        return {

            "status":"synced",

            "direction":"push",

            "source":str(source),

            "destination":str(destination)

        }



    def pull(self, source, destination):

        return self.push(
            source,
            destination
        )



    def status(self, path):

        path = Path(path)


        return {

            "exists":path.exists(),

            "path":str(path)

        }