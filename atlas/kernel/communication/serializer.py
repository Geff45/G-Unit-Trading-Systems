import json
from dataclasses import asdict
from datetime import datetime


class PacketSerializer:

    @staticmethod
    def serialize(packet):

        data = asdict(packet)

        data["timestamp"] = packet.timestamp.isoformat()

        data["signature"] = packet.signature.hex()

        return json.dumps(
            data,
            indent=4,
        )

    @staticmethod
    def deserialize(text):

        data = json.loads(text)

        data["timestamp"] = datetime.fromisoformat(
            data["timestamp"]
        )

        data["signature"] = bytes.fromhex(
            data["signature"]
        )

        return data