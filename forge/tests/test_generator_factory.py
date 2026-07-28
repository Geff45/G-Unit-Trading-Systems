import pytest

from forge.generators import (
    GeneratorFactory,
    ModuleGenerator,
)


def test_factory():

    generator = GeneratorFactory.create(
        "module"
    )

    assert isinstance(
        generator,
        ModuleGenerator,
    )


def test_unknown_generator():

    with pytest.raises(ValueError):

        GeneratorFactory.create(
            "unknown"
        )