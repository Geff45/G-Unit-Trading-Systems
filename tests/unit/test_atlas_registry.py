from gunit.atlas.registry import AtlasRegistry


def test_registry_register():
    registry = AtlasRegistry()

    service = object()

    registry.register("logger", service)

    assert registry.contains("logger")
    assert registry.get("logger") is service