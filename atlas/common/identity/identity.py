from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from common.identity.identity_types import IdentityType


@dataclass(slots=True)
class Identity:

    uid: str

    name: str

    category: IdentityType

    version: str

    created: datetime

    @staticmethod
    def create(
        name: str,
        category: IdentityType,
        version: str = "1.0.0"
    ):

        return Identity(

            uid=str(uuid4()),

            name=name,

            category=category,

            version=version,

            created=datetime.utcnow()
        )