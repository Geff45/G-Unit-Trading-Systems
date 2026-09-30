class SourceRegistry:
    """Registry for independent ATLAS data source instances."""

    def __init__(self):
        self._sources = {}

    def register(self, source):
        self._sources[source.source_id] = source

    def get(self, source_id):
        return self._sources.get(source_id)

    def names(self):
        return list(self._sources)

    def __contains__(self, source_id):
        return source_id in self._sources
