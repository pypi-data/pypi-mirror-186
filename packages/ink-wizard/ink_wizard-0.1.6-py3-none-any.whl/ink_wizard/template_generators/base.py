from jinja2 import Environment, FileSystemLoader
from jinja2.environment import Template
import os


class Base:
    def __init__(self) -> None:
        self.dir_name = ''

    def _create_dir(self, dir_name: str) -> None:
        self.dir_name = dir_name
        os.mkdir(dir_name)

    def _write_file(self, file_name: str, content: str) -> None:
        f = open(self.dir_name + '/' + file_name, "w")
        f.write(content)
        f.close()

    def _get_template_dir(self, dir_name) -> str:
        return os.path.dirname(os.path.realpath(__file__)) + "/../templates/{}/".format(dir_name)

    def _template(self, template_dir: str, template_name: str) -> Template:
        environment = Environment(loader=FileSystemLoader(template_dir))
        return environment.get_template(template_name)

    def _render_content(self, template: Template, **kwargs) -> str:
        return template.render(**kwargs)

    @classmethod
    def generate_code(cls, **kwargs) -> None:
        pass
