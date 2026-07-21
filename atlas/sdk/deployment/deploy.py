"""
Atlas Deployment SDK

Deployment abstraction layer.
"""


class Deploy:


    @staticmethod
    def windows():

        return {

            "platform":"windows",

            "status":"ready"

        }



    @staticmethod
    def linux():

        return {

            "platform":"linux",

            "status":"ready"

        }



    @staticmethod
    def docker():

        return {

            "platform":"docker",

            "status":"ready"

        }



    @staticmethod
    def azure():

        return {

            "platform":"azure",

            "status":"ready"

        }



    @staticmethod
    def aws():

        return {

            "platform":"aws",

            "status":"ready"

        }



    @staticmethod
    def gcp():

        return {

            "platform":"gcp",

            "status":"ready"

        }