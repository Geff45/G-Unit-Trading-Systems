"""
Atlas CLI Registry

Registers developer commands.
"""


class CLI:


    commands = []



    @classmethod
    def register(cls,command):

        cls.commands.append(command)


        return {

            "status":"registered",

            "command":command.name

        }



    @classmethod
    def list(cls):

        return [

            command.name

            for command in cls.commands

        ]