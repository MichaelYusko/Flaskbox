import click

from .helpers import create_init_file


@click.command()
@click.option('--run', is_flag=True, help='Start an your API')
@click.option('--init', is_flag=True, help='Create the Flaskbox file')
@click.option('--start', is_flag=True, help='Run your mock API')
def cli(run, init, start):
    if run:
        print('Your API is running...')
    if init:
        create_init_file()
    if start:
        pass


if __name__ == '__main__':
    cli()
