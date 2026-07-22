import json
from pathlib import Path


MANIFEST = Path("forge_manifest.json")


def load_manifest():

    if not MANIFEST.exists():
        return {
            "version": "0.1.0",
            "installed_phases": []
        }

    return json.loads(
        MANIFEST.read_text(
            encoding="utf-8"
        )
    )


def save_manifest(data):

    MANIFEST.write_text(
        json.dumps(
            data,
            indent=4
        ),
        encoding="utf-8"
    )
