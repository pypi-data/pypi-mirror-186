import mmpos.api.utils as utils


def get():
    farms = utils.call_api("/farms", {}, {})
    for farm in farms:
        farm["sid"] = utils.uuid_hash(farm["id"])
    return farms


def farm_ids():
    return list(map(lambda x: x["id"], get()))


def farms():
    return get()


def default_farm():
    return farms()[0]
