"""
Atlas Hub Server

Core API service.
"""


from routes import Routes



class HubServer:


    def __init__(self):

        self.routes = Routes()



    def start(self):

        return {

            "service":"Atlas Hub",

            "status":"running"

        }



    def register_route(self,name,handler):

        return self.routes.register(
            name,
            handler
        )