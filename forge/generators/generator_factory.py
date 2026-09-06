from .module_generator import ModuleGenerator
from .service_generator import ServiceGenerator
from .plugin_generator import PluginGenerator


class GeneratorFactory:

    @staticmethod
    def create(generator_type, project_root="."):
        """
        Create a generator for the requested component type.
        """

        generator_type = str(generator_type).strip().lower()

        if generator_type == "module":
            return ModuleGenerator(project_root)

        if generator_type == "service":
            return ServiceGenerator(project_root)

        if generator_type == "plugin":
            return PluginGenerator(project_root)

        raise ValueError(
            f"Unknown generator: {generator_type}"
        )