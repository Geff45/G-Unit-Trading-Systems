"""
Manifest Engine
"""

import json
from pathlib import Path


class ManifestEngine:

    def __init__(self, root):

        self.root = Path(root)

        self.file = self.root / "developer-tools" / "guts.manifest.json"

        self.data = None

    def load(self):

        with open(self.file, "r", encoding="utf-8") as file:

            self.data = json.load(file)

        return self.data

    def project(self):

        return self.data["project"]