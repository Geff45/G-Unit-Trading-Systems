from pathlib import Path


class BaseGenerator:

    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)


    def generate(self, *args, **kwargs):
        return None


    def write_file(self, filename, content):

        path = self.output_dir / filename

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            content,
            encoding="utf-8"
        )

        return path
