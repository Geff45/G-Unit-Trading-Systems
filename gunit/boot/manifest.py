from dataclasses import dataclass, field
from typing import List


@dataclass
class PlatformManifest:

    name: str

    version: str

    mode: str

    services: List[str] = field(default_factory=list)

    plugins: List[str] = field(default_factory=list)

    capabilities: List[str] = field(default_factory=list)