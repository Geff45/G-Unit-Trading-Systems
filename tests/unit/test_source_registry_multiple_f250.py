from gunit.data_sources.data_source import DataSource
from gunit.data_sources.source_registry import SourceRegistry


class ExampleSource(DataSource):
    def __init__(self, source_id, source_type):
        self._source_id = source_id
        self._source_type = source_type

    @property
    def source_id(self):
        return self._source_id

    @property
    def source_type(self):
        return self._source_type

    @property
    def capabilities(self):
        return ("quotes",)


def test_registry_keeps_multiple_sources_independent():
    registry = SourceRegistry()

    broker = ExampleSource("broker-a", "market")
    fred = ExampleSource("fred", "economic")

    registry.register(broker)
    registry.register(fred)

    assert registry.get("broker-a") is broker
    assert registry.get("fred") is fred
    assert registry.names() == ["broker-a", "fred"]
    assert len(registry.names()) == 2
