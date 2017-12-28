import click

from flaskbox.generators import YAMLGenerator
from flaskbox.app import application


@click.command()
@click.option('--init', is_flag=True, help='Create the Flaskbox file')
@click.option('--start', is_flag=True, help='Run your mock API')
def cli(init, start):
    if init:
        YAMLGenerator.create_file()
    if start:
        app = application()
        app.run_server()


if __name__ == '__main__':
    cli()
