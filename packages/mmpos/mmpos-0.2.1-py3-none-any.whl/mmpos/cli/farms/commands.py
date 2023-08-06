import click

from prettytable import PrettyTable
import mmpos.api.farms as farms
import json


@click.group()
def entry_point():
    pass


@click.command()
@click.pass_context
def get(ctx):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    data = farms.farms()

    if short_ids:
        id_name = "sid"
    else:
        id_name = "id"
    if format == "table":
        t = PrettyTable()
        t.field_names = ["id", "name", "owner_credits", "own_access_role"]
        for farm in data:
            t.add_row(
                [
                    farm[id_name],
                    farm["name"],
                    farm["owner_credits"],
                    farm["own_access_role"],
                ]
            )
        click.echo(t)
    else:
        click.echo(json.dumps(data, indent=2))


entry_point.add_command(get, "list")
