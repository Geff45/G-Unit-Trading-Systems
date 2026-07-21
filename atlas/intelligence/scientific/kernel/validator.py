import math


class NumericValidator:

    @staticmethod
    def is_valid(value: float) -> bool:
        return (
            value is not None and
            not math.isnan(value) and
            not math.isinf(value)
        )