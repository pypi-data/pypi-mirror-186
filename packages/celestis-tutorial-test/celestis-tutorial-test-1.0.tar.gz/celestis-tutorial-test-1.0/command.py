import click
from create_files import create_project_files

@click.command()
@click.argument("subcommand", required=True)
def celestis(subcommand):
    if subcommand=="start-project":
        project_name = str(input("What is your project name?"))
        create_project_files(project_name)