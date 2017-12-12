import click

from .helpers import create_init_file


@click.command()
@click.option('--run', is_flag=True, help='Start an your API')
@click.option('--init', is_flag=True, help='Create the Flaskbox file')
def cli(run, init):
    if run:
        print('Your API is running...')
    if init:
        create_init_file()


if __name__ == '__main__':
    cli()
