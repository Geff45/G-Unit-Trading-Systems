from typing import Protocol


class Factory(Protocol):
    def __call__(self):
        ...