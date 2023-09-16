import click


@click.group(short_help="dataset_views CLI.")
def dataset_views():
    """dataset_views CLI.
    """
    pass


@dataset_views.command()
@click.argument("name", default="dataset_views")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [dataset_views]
