from gunit.extensions import ExtensionDescriptor


def test_extension_descriptor():

    descriptor = ExtensionDescriptor(
        name="Demo",
        version="1.0.0",
        author="G-Unit",
        description="Demo Extension",
    )

    assert descriptor.name == "Demo"
    assert descriptor.version == "1.0.0"
    assert descriptor.author == "G-Unit"
    assert descriptor.description == "Demo Extension"
