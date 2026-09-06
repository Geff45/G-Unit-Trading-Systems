from .base_generator import BaseGenerator
from .naming import (
    validate_class_name,
    validate_module_name,
)


class ModuleGenerator(BaseGenerator):

    def generate(
        self,
        class_name: str,
        module_name: str,
    ):
        """
        Generate a G-Unit module and its unit test.
        """

        validate_class_name(class_name)
        validate_module_name(module_name)

        module_code = self.templates.render(
            "module.py.tpl",
            {
                "CLASS_NAME": class_name,
            },
        )

        test_code = self.templates.render(
            "module_test.py.tpl",
            {
                "CLASS_NAME": class_name,
                "MODULE_NAME": module_name,
            },
        )

        module = self.write_file(
            f"gunit/modules/{module_name}.py",
            module_code,
        )

        test = self.write_file(
            f"tests/unit/test_{module_name}.py",
            test_code,
        )

        return {
            "module": module,
            "test": test,
        }