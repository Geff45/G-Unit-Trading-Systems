from abc import ABC, abstractmethod

from kernel.service_bus.envelope import Envelope


class Middleware(ABC):
    """
    Base middleware interface.

    Every middleware component receives an
    Envelope, performs its work, and returns
    the (possibly modified) Envelope.
    """

    @abstractmethod
    def process(
        self,
        envelope: Envelope,
    ) -> Envelope:
        """
        Process a message envelope.
        """
        raise NotImplementedError