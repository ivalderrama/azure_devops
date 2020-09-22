import click


@click.command(help="This is just a hello app. It does nothing")
@click.option("--name", prompt="I need your name", help="Need name")
@click.option("--colour", prompt="I need your colour", help="This is your colour")
def hello(name, colour):
    if name == "Thor":
        click.echo("Thor you are always red")
        click.echo(click.style(f"Hello {name}!", fg=f"{colour}"))
    else:
        click.echo(click.style(f"Hello {name}!", fg=f"{colour}"))


if __name__ == '__main__':
    hello()
