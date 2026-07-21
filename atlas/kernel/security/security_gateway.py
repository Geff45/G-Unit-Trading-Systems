from kernel.security.permission import Permission


class SecurityGateway:

    def __init__(self):

        self._permissions = {}

    def grant(self, identity, permission: Permission):

        self._permissions.setdefault(identity, set()).add(permission)

    def authorize(self, identity, permission: Permission):

        return permission in self._permissions.get(identity, set())