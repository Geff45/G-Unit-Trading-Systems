from enum import Enum


class Role(Enum):

    SYSTEM = "system"

    ADMIN = "admin"

    SERVICE = "service"

    AI = "ai"

    USER = "user"

    GUEST = "guest"