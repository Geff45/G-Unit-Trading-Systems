from common.identity.identity import Identity


class IdentityRegistry:

    def __init__(self):

        self._registry = {}

    def register(
        self,
        identity: Identity
    ):

        self._registry[identity.uid] = identity

    def get(self, uid: str):

        return self._registry.get(uid)

    def all(self):

        return list(self._registry.values())

    def count(self):

        return len(self._registry)