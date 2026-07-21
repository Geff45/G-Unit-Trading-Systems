from decimal import Decimal, ROUND_HALF_UP


class Precision:

    DEFAULT_DIGITS = 8

    @staticmethod
    def round(value: float, digits: int = DEFAULT_DIGITS) -> float:
        return float(
            Decimal(str(value)).quantize(
                Decimal("1." + "0" * digits),
                rounding=ROUND_HALF_UP
            )
        )