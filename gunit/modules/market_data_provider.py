from abc import ABC, abstractmethod


class MarketDataProvider(ABC):
    """
    Abstract boundary for market-data providers.
    """

    @abstractmethod
    def get_latest_price(self, symbol: str):
        """
        Return the latest price for a symbol.

        Concrete providers will implement the data-source behavior
        in later milestones.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest_snapshot(self, symbol: str):
        """
        Return the latest market-data snapshot for a symbol.

        Concrete providers will implement the data-source behavior
        in later milestones.
        """
        raise NotImplementedError
