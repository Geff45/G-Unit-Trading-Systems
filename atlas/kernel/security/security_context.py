from dataclasses import dataclass

from kernel.security.role import Role


@dataclass(slots=True)
class SecurityContext:

    identity: str

    role: Role

    authenticated: bool = False