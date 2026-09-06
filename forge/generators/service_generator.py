from .base_generator import BaseGenerator
from .naming import (
    validate_class_name,
    validate_module_name,
)


class ServiceGenerator(BaseGenerator):

    def generate(
        self,
        class_name: str,
        module_name: str,
    ):
        validate_class_name(class_name)
        validate_module_name(module_name)

        service_code = self.templates.render(
            "service.py.tpl",
            {
                "CLASS_NAME": class_name,
            },
        )

        test_code = self.templates.render(
            "service_test.py.tpl",
            {
                "CLASS_NAME": class_name,
                "MODULE_NAME": module_name,
            },
        )

        service = self.write_file(
            f"gunit/services/{module_name}.py",
            service_code,
        )

        test = self.write_file(
            f"tests/unit/services/test_{module_name}.py",
            test_code,
        )

        return {
            "service": service,
            "test": test,
        }