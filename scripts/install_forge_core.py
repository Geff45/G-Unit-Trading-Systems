"""
Forge Core Installer
====================

Creates the Forge development framework.

Usage:
    python scripts/install_forge_core.py
"""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent


class Installer:

    def __init__(self):
        self.created = []
        self.updated = []
        self.skipped = []

    def mkdir(self, path: str):
        target = ROOT / path

        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)
            self.created.append(f"[DIR] {path}")
        else:
            self.skipped.append(f"[DIR] {path}")


    def write(self, path: str, content: str):

        target = ROOT / path

        target.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if target.exists():
            self.updated.append(f"[FILE] {path}")
        else:
            self.created.append(f"[FILE] {path}")

        target.write_text(
            content.strip() + "\n",
            encoding="utf-8"
        )


    def summary(self):

        print("")
        print("==============================")
        print(" Forge Core Installation")
        print("==============================")
        print("")

        for item in self.created:
            print("[CREATED]", item)

        for item in self.updated:
            print("[UPDATED]", item)

        for item in self.skipped:
            print("[SKIPPED]", item)

        print("")
        print("Forge Core installation complete.")
        print("")


installer = Installer()


# -----------------------------
# Folder structure
# -----------------------------

installer.mkdir("forge")
installer.mkdir("forge/generators")
installer.mkdir("forge/templates")
installer.mkdir("forge/utils")

installer.mkdir("tests")
installer.mkdir("tests/forge")

installer.mkdir("docs")
installer.mkdir("docs/forge")


# -----------------------------
# Forge package files
# -----------------------------

installer.write(
    "forge/__init__.py",
    """
__version__ = "0.1.0"

"""
)


installer.write(
    "forge/exceptions.py",
    """
class ForgeError(Exception):
    pass

"""
)


installer.write(
    "forge/filesystem.py",
    """
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def project_root():
    return ROOT

"""
)


installer.write(
    "forge/manifest.py",
    """
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

"""
)


installer.write(
    "forge/renderer.py",
    """
class Renderer:

    def render(self, template, context=None):

        return template

"""
)


installer.write(
    "forge/templates.py",
    """
class TemplateManager:

    def load(self, name):

        return name

"""
)


installer.write(
    "forge/installer.py",
    """
class InstallerEngine:


    def run(self):

        print("Forge installer engine running.")

"""
)


# -----------------------------
# Manifest
# -----------------------------

manifest = {
    "version": "0.1.0",
    "installed_phases": [
        "F001"
    ]
}


(ROOT / "forge_manifest.json").write_text(
    json.dumps(
        manifest,
        indent=4
    ),
    encoding="utf-8"
)


installer.summary()