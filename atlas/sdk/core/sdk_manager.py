"""
Atlas SDK Kernel
"""


class SDK:


    modules = []



    @classmethod
    def register(cls,module):

        cls.modules.append(module)


        return {

            "status":"registered",

            "module":module

        }



    @classmethod
    def info(cls):

        return {

            "modules":cls.modules,

            "count":len(cls.modules)

        }