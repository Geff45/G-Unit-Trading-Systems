from dataclasses import dataclass
from datetime import datetime, UTC
from uuid import uuid4


@dataclass
class SecurePacket:

    packet_id: str

    protocol: str

    sender: str

    receiver: str

    timestamp: datetime

    payload: str

    digest: str

    signature: bytes

    encrypted: bool

    @staticmethod
    def create(
        sender: str,
        receiver: str,
        payload: str,
        digest: str,
        signature: bytes,
        encrypted: bool = True,
    ):

        return SecurePacket(
            packet_id=str(uuid4()),
            protocol="ATLAS-1.0",
            sender=sender,
            receiver=receiver,
            timestamp=datetime.now(UTC),
            payload=payload,
            digest=digest,
            signature=signature,
            encrypted=encrypted,
        )