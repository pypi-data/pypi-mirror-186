import click
from prettytable import PrettyTable
import mmpos.api.rigs as rigs
import mmpos.api.farms as farms
import json
import mmpos.api.utils as utils
import sys


@click.group()
def entry_point():
    pass


@click.command()
@click.option(
    "--farm_id",
    "-f",
    envvar="MMPOS_FARM_ID",
    default="first",
    type=click.STRING,
    required=True,
    help="The id of the farm",
)
@click.option(
    "--rig_id",
    "-r",
    type=click.STRING,
    required=True,
    help="The rig id, not required when using --all or --everywhere flags",
)
@click.option(
    "--profile_ids",
    "-p",
    type=click.STRING,
    required=True,
    multiple=True,
    help="The mining profile ids, can use multiple times.",
)
@click.option(
    "--simulate", is_flag=True, default=False, help="Simulate the action only"
)
@click.pass_context
def set_profiles(ctx, farm_id, rig_id, profile_ids, simulate):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    if farm_id == "first":
        farm_id = farms.farms()[0]["id"]
    rig = rigs.set_profiles(
        farm_id,
        rig_id,
        profile_ids,
        simulate,
    )
    print_rigs([rig], format, short_ids)


def print_rigs(rigs, format, short_ids=False):
    if short_ids:
        id_name = "sid"
        farm_id_name = "farm_sid"
    else:
        id_name = "id"
        farm_id_name = "farm_id"

    if format == "table":
        output = PrettyTable()
        output.field_names = [
            "id",
            "rig_name",
            "address",
            "profiles",
            "agent_version",
            "farm_id",
            "config",
        ]

        for rig in rigs:
            profiles = list(map(lambda x: x["name"], rig["miner_profiles"]))
            output.add_row(
                [
                    rig[id_name],
                    rig["name"],
                    rig["local_addresses"][0],
                    profiles,
                    rig["agent_version"],
                    rig[farm_id_name],
                    rig["active_config"]["name"],
                ]
            )

    else:
        # json data
        output = json.dumps(rigs, indent=2)

    click.echo(output)


@click.command()
@click.option("--all", default=False, help="Show all rigs from all farms", is_flag=True)
@click.option(
    "--farm_id",
    "-f",
    envvar="MMPOS_FARM_ID",
    default="first",
    type=click.STRING,
    help="The id of the farm",
)
@click.pass_context
def get(ctx, all, farm_id):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    if all:
        data = rigs.get("all")
    else:
        if farm_id == "first":
            farm_id = farms.farms()[0]["id"]
        data = rigs.get(farm_id)

    print_rigs(data, format, short_ids)


@click.command()
@click.pass_context
def gpu_table(ctx):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    if short_ids:
        id_name = "sid"
    else:
        id_name = "id"
    if format == "table":
        output = PrettyTable()
        output.field_names = ["rig_name", "name", "address", "gpu_id", "pci_id"]

        for rig in rigs.all_rigs():
            for gpu in rig["gpus"]:
                gpu["sid"] = utils.uuid_hash(gpu["id"])
                output.add_row(
                    [
                        rig["name"],
                        gpu["name"],
                        rig["local_addresses"][0],
                        gpu[id_name],
                        gpu["pci_id"],
                    ]
                )
        click.echo(output)

    else:
        output = []
        for rig in rigs.all_rigs():
            for gpu in rig["gpus"]:
                gpu["sid"] = utils.uuid_hash(gpu["id"])
                output.append(
                    {
                        "rig_name": rig["name"],
                        "name": gpu["name"],
                        "address": rig["local_addresses"][0],
                        "gpu_id": gpu["id"],
                        "gpu_sid": gpu["id"],
                        "pci_id": gpu["pci_id"],
                    }
                )

        click.echo(json.dumps(output, indent=2))


@click.command()
@click.option(
    "--rig_id",
    "-r",
    type=click.STRING,
    help="The rig id, not required when using --all or --everywhere flags",
)
@click.option(
    "--farm_id",
    "-f",
    type=click.STRING,
    default="first",
    show_default=True,
    help="The farm id, defaults to first farm found, use '--all' flag for all farms",
)
@click.option(
    "--all",
    default=False,
    help="Run action on all rigs across the entire farm",
    is_flag=True,
)
@click.option(
    "--everywhere",
    default=False,
    help="Danger: Run action on all rigs across all farms",
    is_flag=True,
)
@click.option(
    "--action",
    required=True,
    type=click.Choice(
        ["disable", "poweroff", "reset", "enable", "restart", "reboot"],
        case_sensitive=False,
    ),
)
@click.option(
    "--simulate", is_flag=True, default=False, help="Simulate the action only"
)
@click.pass_context
def rig_control(ctx, action, rig_id, farm_id, all, everywhere, simulate):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    farm_ids = []
    if farm_id == "first":
        farm_ids = [farms.default_farm()["id"]]
    elif farm_id:
        farm_ids = [farm_id]
    elif everywhere:
        farm_ids = farms.farm_ids()
    else:
        farm_ids = []

    output = []

    if format == "table":
        output = PrettyTable()
        output.field_names = ["rig_name", "action"]
        format_block = lambda name, action: output.add_row([name, action])
    elif format == "json":
        output = []
        format_block = lambda name, action: output.append(
            {"rig_name": name, "action": action}
        )
    else:
        format_block = lambda name, action: output.append(
            f"{name} has been set to {action}"
        )

    if not rig_id and (all or everywhere):
        # run_output = list(map(rigs.rig_control, action, "all", farm_id, simulate=simulate, block=format_block ))
        for farm_id in farm_ids:
            rigs.rig_control(
                action, "all", farm_id, simulate=simulate, block=format_block
            )
    else:
        rigs.rig_control(action, rig_id, farm_id, simulate=simulate, block=format_block)

    if format == "table":
        click.echo(output)
    elif format == "json":
        click.echo(json.dumps(output, indent=2))
    else:
        click.echo("\n".join(output))


@click.command
@click.option(
    "--rig_id",
    "-r",
    type=click.STRING,
    help="The rig id, not required when using --all or --everywhere flags",
)
@click.option(
    "--farm_id",
    "-f",
    type=click.STRING,
    default="first",
    show_default=True,
    help="The farm id, defaults to first farm found, use '--all' flag for all farms",
)
@click.pass_context
def list_configs(ctx, farm_id, rig_id):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    output = ""
    if farm_id == "first":
        farm_id = farms.farms()[0]["id"]

    if short_ids:
        id_name = "sid"
        rig_id_name = "rig_sid"

    else:
        id_name = "id"
        rig_id_name = "rig_id"

    if format == "table":
        output = PrettyTable()
        output.field_names = [
            "config_id",
            "config_name",
            "rig_id",
            "rig_name",
            "active",
        ]

        rigs.list_configs(
            rig_id,
            farm_id,
            lambda config: {
                output.add_row(
                    [
                        config[id_name],
                        config["name"],
                        config[rig_id_name],
                        config["rig_name"],
                        "*" if config["active"] else "",
                    ]
                )
            },
        )

    else:
        # json data
        output = json.dumps(rigs.list_configs(rig_id, farm_id), indent=2)

    click.echo(output)


@click.command
@click.option(
    "--rig_id",
    "-r",
    required=False,
    type=click.STRING,
    help="The rig id, not required when using --all or --everywhere flags",
)
@click.option(
    "--farm_id",
    "-f",
    type=click.STRING,
    default="first",
    show_default=True,
    help="The farm id, defaults to first farm found, use '--all' flag for all farms",
)
@click.option(
    "--config-id",
    type=click.STRING,
    required=True,
    help="The config id or name to assign to the rig",
)
@click.pass_context
def set_config(ctx, rig_id, farm_id, config_id):
    format = ctx.parent.obj["format"]
    short_ids = ctx.parent.obj["short_ids"]
    output = ""
    if farm_id == "first":
        farm_id = farms.farms()[0]["id"]
    rig = rigs.activate_config(rig_id, farm_id, config_id)
    print_rigs([rig], format, short_ids)


entry_point.add_command(set_config, "set-config")
entry_point.add_command(list_configs, "configs")
entry_point.add_command(gpu_table, "gpus")
entry_point.add_command(rig_control, "control")
entry_point.add_command(get, "list")
entry_point.add_command(set_profiles, "set-profiles")
