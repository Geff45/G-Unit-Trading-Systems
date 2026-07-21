"""
Atlas Result Store

Keeps execution results.
"""


class ResultStore:


    def __init__(self):

        self.results = []



    def save(self, result):

        self.results.append(result)

        return result



    def all(self):

        return self.results