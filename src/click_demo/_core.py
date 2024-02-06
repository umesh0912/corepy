import click

@click.command()
@click.option('--name', default='Umesh', help='The person to greet.')
def greet(name):
    click.echo(f'Hello, {name}!')