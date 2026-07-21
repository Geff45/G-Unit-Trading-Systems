from dataclasses import dataclass


@dataclass(slots=True)
class Vector:

    values: list[float]

    def magnitude(self):

        return sum(x * x for x in self.values) ** 0.5

    def dot(self, other):

        return sum(a * b for a, b in zip(self.values, other.values))