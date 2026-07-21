from dataclasses import dataclass


@dataclass(slots=True)
class TrendMetrics:

    direction: float

    strength: float

    persistence: float

    acceleration: float

    pullback_quality: float

    confidence: float