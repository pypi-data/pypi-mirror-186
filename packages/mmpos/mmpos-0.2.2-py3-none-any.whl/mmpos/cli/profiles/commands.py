import click
from prettytable import PrettyTable
import mmpos.api.profiles as profiles
import mmpos.api.farms as farms
import json


@click.group()
def entry_point():
    pass


@click.command()
@click.pass_context
@click.option(
    "--all", default=False, help="Show all mining_profiles from all farms", is_flag=True
)
@click.option(
    "--farm_id",
    "-f",
    envvar="MMPOS_FARM_ID",
    default="first",
    type=click.STRING,
    help="The id of the farm",
)
def get(ctx, all, farm_id):
    output = ""
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    if short_ids:
        farm_id_name = "farm_sid"
        id_name = "sid"
    else:
        farm_id_name = "farm_id"
        id_name = "id"
    if all:
        data = profiles.get_all()
    else:
        if farm_id == "first":
            farm_id = farms.farms()[0]["id"]
        data = profiles.get(farm_id)

    if format == "table":
        output = PrettyTable()
        output.field_names = ["id", "name", "coin", "os", "farm_id"]

        for profile in data:
            output.add_row(
                [
                    profile[id_name],
                    profile["name"],
                    profile["coin"],
                    profile["os"],
                    profile[farm_id_name],
                ]
            )

    else:
        # json data
        output = json.dumps(data, indent=2)

    click.echo(output)


entry_point.add_command(get, "list")
