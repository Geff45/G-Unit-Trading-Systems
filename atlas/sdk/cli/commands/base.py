"""
Atlas CLI Command Base
"""


class Command:


    def __init__(self,name):

        self.name = name



    def execute(self):

        return {

            "command":self.name,

            "status":"executed"

        }