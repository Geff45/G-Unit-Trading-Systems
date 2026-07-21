"""
Atlas Hub Routes

Defines available Hub operations.
"""


class Routes:


    def __init__(self):

        self.routes = []



    def register(self, name, handler):

        self.routes.append(
            {
                "name": name,
                "handler": handler
            }
        )


        return {
            "status":"registered",
            "route":name
        }



    def list(self):

        return self.routes