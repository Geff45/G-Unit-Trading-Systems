from dataclasses import dataclass


@dataclass(slots=True)
class Matrix:

    values: list[list[float]]

    @property
    def rows(self):

        return len(self.values)

    @property
    def columns(self):

        if not self.values:

            return 0

        return len(self.values[0])