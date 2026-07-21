class EvidenceRegistry:
    
    def __init__(self):

        self._evidence = []

    def add(self, evidence):

        self._evidence.append(evidence)

    def all(self):

        return list(self._evidence)

    def count(self):

        return len(self._evidence)

    def clear(self):

        self._evidence.clear()