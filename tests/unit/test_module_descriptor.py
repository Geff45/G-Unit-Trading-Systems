from gunit.modules import ModuleDescriptor


def test_descriptor():
    descriptor = ModuleDescriptor(
        name="Trading",
        version="2.0.0",
    )

    assert descriptor.name == "Trading"
    assert descriptor.version == "2.0.0"