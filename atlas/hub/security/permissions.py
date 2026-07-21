"""
Atlas Permissions

Controls access rights.
"""


class Permissions:


    def __init__(self):

        self.roles = {}



    def assign(self,user,role):

        self.roles[user] = role


        return {

            "user":user,

            "role":role

        }



    def check(self,user,role):

        return self.roles.get(user) == role