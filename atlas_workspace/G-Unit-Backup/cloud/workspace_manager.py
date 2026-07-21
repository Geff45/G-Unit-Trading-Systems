"""
Atlas Workspace Manager

Controls creation and management
of Atlas cloud workspaces.
"""


from pathlib import Path



class WorkspaceManager:


    def __init__(self, root="./atlas_workspace"):

        self.root = Path(root)

        self.root.mkdir(
            parents=True,
            exist_ok=True
        )


    def create(self, name):

        workspace = self.root / name

        workspace.mkdir(
            exist_ok=True
        )


        return {
            "status":"created",
            "workspace":str(workspace)
        }



    def exists(self, name):

        workspace = self.root / name

        return workspace.exists()



    def list(self):

        return [
            item.name
            for item in self.root.iterdir()
            if item.is_dir()
        ]



    def delete(self,name):

        workspace = self.root / name


        if workspace.exists():

            for item in workspace.iterdir():

                if item.is_file():

                    item.unlink()


            workspace.rmdir()


            return {
                "status":"deleted"
            }


        return {
            "status":"not_found"
        }