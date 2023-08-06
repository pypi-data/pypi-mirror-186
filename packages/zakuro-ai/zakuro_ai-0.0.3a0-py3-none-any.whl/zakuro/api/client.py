import requests
from gnutools.utils import id_generator
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
import base64
import cv2
import sys
import hashlib
import json
from datetime import datetime

db = {"tasks": {}, "data": set()}


class TaskAPIClient:
    def __init__(self, host, port):
        self.endpoint = f"http://{host}:{port}"

    def wait(self, id, d):
        # disable_cache = d["meta"]["hash"] not in cache
        disable_cache = False
        key = d["meta"]["hash"]
        if disable_cache or not key in db["tasks"]:
            self.insert(id, d)
            output = self.get(id)
            db["tasks"][key] = output
        else:
            output = db["tasks"][key]
        return output

    def select_all(self):
        r = requests.get(self.endpoint)
        return json.loads(r.content.decode())

    def insert(self, id, d):
        r = requests.post(f"{self.endpoint}/tasks/{id}", json=d)
        if r.content.decode().__contains__("Exception"):
            raise AssertionError
        else:
            return True

    def store(self, img):
        d = {}
        d.setdefault("fingerprint", f"zakuro::{hashlib.md5(img).hexdigest()}")
        if not d["fingerprint"] in db["data"]:
            d.setdefault("dtype", str(img.dtype))
            d.setdefault("shape", img.shape)
            d.setdefault("data", str(base64.b64encode(img)))
            r = requests.post(f'{self.endpoint}/data/{d["fingerprint"]}', json=d)
            if r.content.decode().__contains__("Exception"):
                raise AssertionError
            db["data"].add(d["fingerprint"])
        return d["fingerprint"]

    def get(self, id):
        r = requests.get(f"{self.endpoint}/tasks/{id}")
        if r.content.decode().__contains__("Exception"):
            raise AssertionError
        else:
            return json.loads(r.content.decode())


img = cv2.imread("/mnt/.cpj/ZAK/zak-python/lena.png")


def main(id, client):
    d = {
        "module": "zakuro.cv2",
        "function": "main",
        "args": ["hello world"],
        "kwargs": {"img": client.store(img)},
    }
    hash = hashlib.md5(str(d).encode()).hexdigest()
    d["meta"] = {"size": sys.getsizeof(d), "hash": hash}
    output = client.wait(id, d)
    return output["result"], output["logger"]


if __name__ == "__main__":
    N = 1000
    import random

    ids = list(
        set(
            [
                f"zakuro::{hashlib.md5(str(id_generator(12) + datetime.now().__str__()).encode()).hexdigest()}"
                for _ in range(N)
            ]
        )
    )
    clients = [
        TaskAPIClient("127.0.0.1", random.randrange(9000, 9001)) for _ in range(N)
    ]
    assert len(ids) == N
    # [main(id, client) for id, client in tqdm(zip(ids, clients), total=len(ids), desc="Retrieving the resuluts")]
    with ProcessPoolExecutor(12) as e:
        fs = [e.submit(main, id, client) for id, client in zip(ids, clients)]
        for f in tqdm(as_completed(fs), total=len(fs), desc="Retrieving the resuluts"):
            assert f._exception is None
            # print(f._result)
# #
