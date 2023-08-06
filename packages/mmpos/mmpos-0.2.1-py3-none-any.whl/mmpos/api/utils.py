import json
import urllib
import os
from requests_cache import CachedSession
import hashlib
from functools import wraps
import pickle
from platformdirs import user_cache_dir

MMPOS_API_URL = "https://api.mmpos.eu"
MAX_THREAD_COUNT = 15
CACHE_PATH = user_cache_dir("mmpos_object_cache")


def call_api(path, params={"limit": 100}, data={}, method="GET"):
    session = CachedSession(
        cache_name="mmpos_cache",
        backend="filesystem",
        serializer="json",
        expire_after=360,  # 5 minutes
        allowable_methods=["GET"],
        use_cache_dir=True,
    )
    headers = {
        "X-API-Key": os.environ["MMPOS_API_TOKEN"],
        "Content-Type": "application/json",
    }
    url = urllib.parse.urljoin(MMPOS_API_URL, f"api/v1/{path}")
    try:
        if method == "GET":
            response = session.get(
                url, params=params, headers=headers, data=json.dumps(data)
            )
        elif method == "POST":
            response = session.post(
                url, params=params, headers=headers, data=json.dumps(data)
            )
        else:
            # method not supported
            raise Exception(f"method {method} is not supported")

        data = response.json()

    except json.decoder.JSONDecodeError:
        if response.ok:
            data = response.content

    return data


def flatten(x):
    return [i for row in x for i in row]


def current_thread_count(items):
    active_threads = 0
    for item in items:
        if item.is_alive():
            active_threads = active_threads + 1

    return active_threads


def read_cache_file():
    try:
        with open(CACHE_PATH, "rb") as f:
            # print("Reading cache to file")
            cache = pickle.load(f)

    except FileNotFoundError:
        cache = {}
    except EOFError:
        cache = {}
    return cache


def cached(func):
    func.cache = read_cache_file()

    @wraps(func)
    def wrapper(*args):
        try:
            return func.cache[args]
        except KeyError:
            result = func(*args)
            func.cache[result] = args[0]
            return result

    return wrapper


@cached
def uuid_hash(str):
    if len(str) == 8:
        return str
    return hashlib.shake_256(str.encode()).hexdigest(4)


def shorten(obj):
    """Takes in the object and finds anything with an id and shortens it"""
    if type(obj) is not dict:
        return obj
    if "id" in obj:
        obj["sid"] = uuid_hash(obj["id"])
    for v in dict(obj).values():
        if type(v) is dict:
            v = shorten(v)
        if type(v) is list:
            for x in v:
                x = shorten(x)

    return obj


def from_uuid_hash(str):
    try:
        if len(str) == 36:
            uuid = str
        else:
            uuid = uuid_hash.cache[str]
    except KeyError as e:
        return str
    return uuid


def cache_commit():
    with open(CACHE_PATH, "wb") as f:
        # print(f'Writing cache to file to {CACHE_PATH}')
        f.write(pickle.dumps(uuid_hash.cache))
