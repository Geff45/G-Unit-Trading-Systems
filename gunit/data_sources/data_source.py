from abc import ABC, abstractmethod


class DataSource(ABC):
    """Abstract boundary for an external ATLAS data source."""

    @property
    @abstractmethod
    def source_id(self) -> str:
        """Return the stable identity of this data source."""
        raise NotImplementedError

    @property
    @abstractmethod
    def source_type(self) -> str:
        """Return the category/type of this data source."""
        raise NotImplementedError

    @property
    @abstractmethod
    def capabilities(self) -> tuple[str, ...]:
        """Return the capabilities declared by this data source."""
        raise NotImplementedError
