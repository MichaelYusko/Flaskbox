import click


@click.command()
@click.option('--run', is_flag=True, help="Start an your API")
def cli(run):
    if run:
        print('Your API is running...')


if __name__ == '__main__':
    cli()
