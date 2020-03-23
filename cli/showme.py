import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--num', '-n', type=int, default=5)
def email(num):
    print("Hello World", num)

@cli.command()
def weather():
    print("weather toggled")