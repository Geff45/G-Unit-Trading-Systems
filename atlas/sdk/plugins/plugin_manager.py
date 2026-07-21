"""
Atlas Plugin SDK

Manages extensions.
"""


class Plugin:


    plugins = {}



    @classmethod
    def install(cls,name):

        cls.plugins[name] = {

            "status":"installed"

        }


        return {

            "plugin":name,

            "status":"installed"

        }



    @classmethod
    def load(cls,name):

        if name in cls.plugins:

            cls.plugins[name]["status"] = "loaded"


        return {

            "plugin":name,

            "status":"loaded"

        }



    @classmethod
    def enable(cls,name):

        if name in cls.plugins:

            cls.plugins[name]["status"] = "enabled"


        return {

            "plugin":name,

            "status":"enabled"

        }



    @classmethod
    def disable(cls,name):

        if name in cls.plugins:

            cls.plugins[name]["status"] = "disabled"


        return {

            "plugin":name,

            "status":"disabled"

        }