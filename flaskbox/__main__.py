import click

from flaskbox.generators import YamlGenerator


@click.command()
@click.option('--run', is_flag=True, help='Start an your API')
@click.option('--init', is_flag=True, help='Create the Flaskbox file')
@click.option('--start', is_flag=True, help='Run your mock API')
def cli(run, init, start):
    if run:
        pass
    if init:
        YamlGenerator.create_file()
    if start:
        pass


if __name__ == '__main__':
    cli()
