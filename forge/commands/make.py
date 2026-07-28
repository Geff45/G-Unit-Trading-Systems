from forge.console import Console
from forge.generators import GeneratorFactory


def execute(generator_name, class_name):

    module_name = (
        class_name
        .replace(" ", "_")
        .lower()
    )

    generator = GeneratorFactory.create("module")

    result = generator.generate(
        class_name=class_name,
        module_name=module_name,
    )

    Console.success("Generation completed.")
    Console.write("")
    Console.write(result["module"])
    Console.write(result["test"])