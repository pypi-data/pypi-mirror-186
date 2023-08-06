import typer

from .commands.template_select import TemplateSelectCommand
from .commands.flipper import FlipperCommand
from .commands.psp22 import PSP22Command
from .commands.psp34 import PSP34Command
from .commands.psp37 import PSP37Command

def main() -> None:
    
    TemplateSelectCommand.show_options()

    contract_type = TemplateSelectCommand.ask_user()

    if contract_type == "1":
        FlipperCommand.run_command()
    if contract_type == "2":
        PSP22Command.run_command()
    if contract_type == "3":
        PSP34Command.run_command()
    if contract_type == "4":
        PSP37Command.run_command()

if __name__ == "__main__":
    typer.run(main)
