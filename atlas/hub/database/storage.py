"""
Atlas Storage Engine

Stores system records.
"""


class Storage:


    def __init__(self):

        self.records = []



    def save(self,item):

        self.records.append(
            item
        )

        return {

            "status":"saved",

            "item":item

        }



    def all(self):

        return self.records