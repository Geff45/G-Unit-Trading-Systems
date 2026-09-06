from forge.generators import (
    GeneratorFactory,
    ModuleGenerator,
    ServiceGenerator,
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

    try:
        GeneratorFactory.create(
            "unknown"
        )
    except ValueError as exc:
        assert "Unknown generator" in str(exc)
    else:
        raise AssertionError(
            "Expected ValueError for unknown generator"
        )


def test_service_generator_factory():

    generator = GeneratorFactory.create(
        "service"
    )

    assert isinstance(
        generator,
        ServiceGenerator,
    )