from datetime import datetime

from intelligence.core.evidence import Evidence
from intelligence.core.evidence_registry import EvidenceRegistry
from intelligence.core.evidence_fusion import EvidenceFusion
from intelligence.core.world_model import WorldModel


registry = EvidenceRegistry()

registry.add(
    Evidence(
        source="RSI",
        category="Momentum",
        instrument="EURUSD",
        direction=0.8,
        confidence=0.70,
        weight=0.50,
        timestamp=datetime.utcnow(),
        metadata={}
    )
)

registry.add(
    Evidence(
        source="VWAP",
        category="Trend",
        instrument="EURUSD",
        direction=0.90,
        confidence=0.90,
        weight=0.80,
        timestamp=datetime.utcnow(),
        metadata={}
    )
)

fusion = EvidenceFusion()

bias = fusion.fuse(registry.all())

world = WorldModel()

world.instrument_states["EURUSD"] = {
    "technical_bias": bias
}

print("Evidence:", registry.count())
print("Bias:", bias)
print(world.instrument_states)