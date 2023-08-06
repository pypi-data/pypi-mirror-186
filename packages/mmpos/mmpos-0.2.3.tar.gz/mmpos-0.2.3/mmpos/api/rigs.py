import mmpos.api.utils as utils
import threading
import mmpos.api.farms as farms

rig_name_table = {}


def get(farm_id):
    data = []
    if farm_id == "all":
        for farm in farms.farms():
            data.append(rigs(farm["id"]))
        return utils.flatten(data)
    else:
        data = rigs(farm_id)

    return data


def all_rigs():
    return get("all")


def rig_name_list(refresh=False):
    if len(rig_name_table) < 1 or refresh:
        for rig in all_rigs():
            rig_name_table[rig["id"]] = rig["name"]

    return rig_name_table


def get_rig(farm_id, rig_id):
    data = utils.call_api(f"{farm_id}/rigs/{rig_id}")
    data = utils.shorten(data)
    data["farm_sid"] = utils.uuid_hash(farm_id)
    return data


def rigs(farm_id):
    farm_sid = utils.uuid_hash(farm_id)
    rigs = utils.call_api(f"{farm_id}/rigs")
    for rig in rigs:
        rig["farm_sid"] = farm_sid
        rig["sid"] = utils.uuid_hash(rig["id"])

    return rigs


def set_rig_control(action, farm_id, rig_id, simulate=False, block=None):
    if not simulate:
        resp = utils.call_api(
            f"{farm_id}/rigs/{rig_id}/control", {}, {"control": action}, method="POST"
        )
    else:
        action = f"simulated-{action}"
    if block:
        rig_name = rig_name_list()[rig_id]
        block(rig_name, f"{action}")

    resp = get_rig(farm_id, rig_id)
    return resp


def set_profiles(farm_id, rig_id, profile_ids, simulate, block=lambda x, y: {}):
    farm_id = utils.from_uuid_hash(farm_id)
    rig_id = utils.from_uuid_hash(rig_id)
    pids = list(map(utils.from_uuid_hash, (profile_ids)))
    data = {"miner_profiles": pids}
    path = f"{farm_id}/rigs/{rig_id}/miner_profiles"
    action = "set mining profile"
    rig_name = rig_name_list()[rig_id]

    if simulate:
        out = f"simulated-{action}"
        rig = get_rig(farm_id, rig_id)
    else:
        rig = utils.call_api(path=path, params={}, data=data, method="POST")
        if "code" in rig:
            raise Exception(rig)
        else:
            out = action

    block(rig_name, out)
    rig["farm_id"] = farm_id
    rig["farm_sid"] = utils.uuid_hash(farm_id)

    return utils.shorten(rig)


def rig_control(action, rig_id, farm_id, simulate=False, block=None):
    farm_id = utils.from_uuid_hash(farm_id)
    rig_id = utils.from_uuid_hash(rig_id)
    resp = ""
    if rig_id == "all":
        threads = []
        for rig in rigs(farm_id):
            x = threading.Thread(
                target=set_rig_control,
                args=(action.lower(), farm_id, rig["id"]),
                kwargs={"simulate": simulate, "block": block},
            )
            if utils.current_thread_count(threads) > utils.MAX_THREAD_COUNT:
                threads.pop(0).join()  # wait for the first thread to finish

            x.start()
            threads.append(x)  # add to bottom of list
        # Wait for any last threads
        for x in threads:
            x.join()
    else:
        resp = set_rig_control(
            action.lower(), farm_id, rig_id, simulate=simulate, block=block
        )

    return resp


def find_config(rig_id, farm_id, config_id):
    farm_id = utils.from_uuid_hash(farm_id)
    rig_id = utils.from_uuid_hash(rig_id)
    rig = get_rig(farm_id, rig_id)
    found_config = {}
    for config in rig["configs"]:
        if (
            config["name"].lower() == config_id.lower() or config["id"] == config_id
        ) or config["sid"] == config_id:
            found_config = config
            break
    return found_config


def activate_config(rig_id, farm_id, config_id):
    farm_id = utils.from_uuid_hash(farm_id)
    rig_id = utils.from_uuid_hash(rig_id)
    try:
        config = find_config(rig_id, farm_id, config_id)
        found_id = config["id"]
    except KeyError:
        # config name not found
        raise Exception(
            f"The config id {config_id} is not usable for this rig, check spelling or id"
        )

    rig = utils.call_api(
        path=f"{farm_id}/rigs/{rig_id}/configs/{found_id}/activate", method="POST"
    )
    rig["farm_id"] = farm_id
    rig["farm_sid"] = utils.uuid_hash(farm_id)
    return utils.shorten(rig)


def list_configs(rig_id=None, farm_id="all", block=None):
    configs = []
    if rig_id:
        rigs = [get_rig(rig_id)]
    else:
        rigs = get(farm_id)

    for rig in rigs:
        for config in rig["configs"]:

            config = utils.shorten(config)
            config["rig_id"] = rig["id"]
            config["rig_sid"] = rig["sid"]
            config["rig_name"] = rig["name"]
            config["active"] = rig["active_config"]["id"] == config["id"]
            configs.append(config)
            if block:
                block(config)

    return configs
