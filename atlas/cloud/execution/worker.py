"""
Atlas Worker

Executes scheduled tasks.
"""


class Worker:


    def run(self, task):

        return {

            "task":task,

            "status":"completed"

        }