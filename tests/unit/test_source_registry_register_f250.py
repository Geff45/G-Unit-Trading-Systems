from gunit.data_sources.data_source import DataSource
from gunit.data_sources.source_registry import SourceRegistry


class ExampleSource(DataSource):
    @property
    def source_id(self):
        return "example-source"

    @property
    def source_type(self):
        return "market"

    @property
    def capabilities(self):
        return ("quotes",)


def test_registry_registers_and_retrieves_data_source():
    registry = SourceRegistry()
    source = ExampleSource()

    registry.register(source)

    assert registry.get("example-source") is source
