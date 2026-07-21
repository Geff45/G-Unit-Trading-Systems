"""
Atlas Service SDK

Manages application services.
"""


class Service:


    services = {}



    @classmethod
    def create(cls,name):

        cls.services[name] = {

            "status":"created"

        }


        return {

            "service":name,

            "status":"created"

        }



    @classmethod
    def start(cls,name):

        if name in cls.services:

            cls.services[name]["status"] = "running"


        return {

            "service":name,

            "status":"running"

        }



    @classmethod
    def stop(cls,name):

        if name in cls.services:

            cls.services[name]["status"] = "stopped"


        return {

            "service":name,

            "status":"stopped"

        }



    @classmethod
    def health(cls,name):

        return cls.services.get(

            name,

            {

                "status":"unknown"

            }

        )