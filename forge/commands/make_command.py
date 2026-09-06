from forge.framework import Command, CommandResult, CommandContext
from forge.generators import GeneratorFactory
from forge.generators.naming import to_module_name


class MakeCommand(Command):

    name = "make"

    def execute(self, context):

        args = (
            context.args
            if isinstance(context, CommandContext)
            else context
        )

        if len(args) < 2:
            return CommandResult.fail(
                "Usage: forge make <type> <name>"
            )

        generator_type = args[0]
        name = args[1]

        if isinstance(context, CommandContext):
            project_root = context.working_directory
        else:
            project_root = "."

        try:
            generator = GeneratorFactory.create(
                generator_type,
                project_root,
            )

            if generator_type.strip().lower() == "plugin":
                result = generator.generate(name)
            else:
                module_name = to_module_name(name)

                result = generator.generate(
                    class_name=name,
                    module_name=module_name,
                )

        except (ValueError, FileExistsError) as exc:
            return CommandResult.fail(str(exc))

        return CommandResult.ok(
            f"Generated {generator_type}: {name}",
            result,
        )
