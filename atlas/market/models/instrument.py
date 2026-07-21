from dataclasses import dataclass


@dataclass(slots=True)
class Instrument:

    symbol: str

    asset_class: str

    digits: int

    point: float

    contract_size: float

    currency: str