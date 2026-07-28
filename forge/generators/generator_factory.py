from .module_generator import ModuleGenerator


class GeneratorFactory:

    _generators = {
        "module": ModuleGenerator,
    }

    @classmethod
    def create(
        cls,
        generator_type: str,
        project_root=".",
    ):
        generator_type = generator_type.lower()

        if generator_type not in cls._generators:
            raise ValueError(
                f"Unknown generator '{generator_type}'."
            )

        return cls._generators[generator_type](
            project_root
        )