import re

from .base_generator import BaseGenerator


class PluginGenerator(BaseGenerator):

    def generate(self, name):

        if not isinstance(name, str) or not re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*",
            name,
        ):
            raise ValueError(
                f"Invalid plugin name: {name!r}"
            )

        plugins_directory = self.project_root / "plugins"
        plugins_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        init_file = plugins_directory / "__init__.py"

        if not init_file.exists():
            self.write_file(
                "plugins/__init__.py",
                "",
            )

        plugin_file = plugins_directory / f"{name}.py"

        if plugin_file.exists():
            raise FileExistsError(
                f"Plugin already exists: {plugin_file}"
            )

        self.write_file(
            f"plugins/{name}.py",
            f'"""Generated Forge plugin: {name}."""\n',
        )

        return plugin_file
