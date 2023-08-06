import click
import os
from mmpos.cli.rigs import commands as rigs
from mmpos.cli.farms import commands as farms
from mmpos.cli.profiles import commands as profiles
import sys
import mmpos.api.utils as utils
import traceback


@click.group()
@click.version_option(version="0.2.3", prog_name="mmpos cli")
@click.option(
    "--table", "format", default=True, help="Show table output", flag_value="table"
)
@click.option(
    "--json", "format", default=False, help="Show json output", flag_value="json"
)
@click.option(
    "--plain", "format", default=False, help="Show plain output", flag_value="plain"
)
@click.option(
    "--short-ids/--no-short-ids",
    default=True,
    show_default=True,
    help="Use short id instead of uuid from mmpos",
)
@click.pass_context
def entry_point(ctx, format, short_ids):
    ctx.obj = {"format": format, "short_ids": short_ids}


entry_point.add_command(rigs.entry_point, "rigs")
entry_point.add_command(farms.entry_point, "farms")
entry_point.add_command(profiles.entry_point, "profiles")


def main(prog_name="mmpos"):
    try:
        os.environ["MMPOS_API_TOKEN"]
        entry_point()
    except KeyError as e:
        if "MMPOS_API_TOKEN" in f"{e}":
            print("MMPOS_API_TOKEN environment variable not set")
        else:
            print(e)
        sys.exit(1)
    except Exception as e:
        print(e)
        traceback.print_exc()
        sys.exit(1)
    finally:
        utils.cache_commit()
