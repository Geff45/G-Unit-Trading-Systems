"""
Atlas Authentication System

Handles user identity.
"""


class Auth:


    def __init__(self):

        self.users = {}



    def register(self, username):

        self.users[username] = {

            "active": True

        }


        return {

            "status":"registered",

            "user":username

        }



    def verify(self, username):

        return self.users.get(
            username,
            {
                "active":False
            }
        )