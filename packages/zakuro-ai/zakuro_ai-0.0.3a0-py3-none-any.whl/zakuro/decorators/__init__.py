from gnutools.utils import id_generator
import json
import os
import time
from .functional import *
import requests
import psutil


class TaskManager:
    def __init__(self, root="/tmp/zakuro/run"):
        self.root = root
        self.init()

    def init(self):
        self._result = None
        self._id = id_generator()
        os.makedirs(self.root, exist_ok=True)

    def submit(self, func, *args, **kwargs):
        self.init()
        run_file = f"{self.root}/todo/{self._id}.json"
        d = {
            "module": get_module(func),
            "function": func.__name__,
            "args": args,
            "kwargs": kwargs,
        }
        url = "http://127.0.0.1:8000/todo"
        json.dump(d, open(run_file, "w"), indent=4)
        # res = requests.get(f"{url}/{str(json.dumps(d))}")
        res = requests.post(f"{url}/{self._id}")

    def join(self):
        run_file = f"{self.root}/done/{self._id}.json"
        while not os.path.exists(run_file):
            time.sleep(1)
        data = json.load(open(run_file, "r"))
        print("\n".join(data["logger"]))
        return data["result"]


def p2p(func):
    """

    :param fcn:
    :return:
    """

    def wrapper(*args, **kwargs):
        # Remote
        c1 = not "__force_local__" in kwargs
        c2 = len(get_module(func)) > 0
        if c1 and c2:
            task_manager = TaskManager()
            task_manager.submit(func, *args, **kwargs)
            task_manager.join()
            result = task_manager._result
        # Local
        else:
            if not c1:
                del kwargs["__force_local__"]
            result = func(*args, **kwargs)
        return result

    return wrapper


def limit_mem(percentage=100, timeout=30):
    def multipass(func):
        def wrapper(*args, **kw):
            elapsed = 0
            while psutil.virtual_memory()[2] >= percentage:
                time.sleep(1)
                if timeout is not None:
                    elapsed+=1
                    if elapsed>=timeout:
                        raise TimeoutError
            return func(*args, **kw)

        return wrapper

    return multipass
