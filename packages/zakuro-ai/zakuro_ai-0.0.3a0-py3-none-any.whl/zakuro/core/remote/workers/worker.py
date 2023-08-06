from threading import Thread
from gnutools.fs import listfiles, name
import random
import os
import json
import time
from datetime import datetime

from io import StringIO
import sys


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class Worker(Thread):
    def __init__(self, root="/tmp/zakuro/run"):
        super(Worker, self).__init__()
        self.root = root
        self.pid = os.getpid()
        self.delay = 1
        self.logger = None
        self.result = None
        [os.makedirs(f"{self.root}/{c}", exist_ok=True) for c in ["todo", "doing", "done"]]

    def nap(self):
        time.sleep(self.delay)
        print(f"{datetime.now()}| Worker {self.pid} >> Sleeping for {self.delay} seconds")

    def run(self):
        while True:
            candidates = listfiles(f"{self.root}/todo", [".json"])
            try:
                assert len(candidates)>0
                self.pop(candidates)
            except AssertionError:
                pass
            finally:
                self.nap()

    def pop(self, candidates):
        run_file = random.sample(candidates, 1)[0]
        # Doing
        task, _, run_file = json.load(open(f"{self.root}/todo/{name(run_file)}.json", "r")), \
                            os.system(f"mv {run_file} {self.root}/doing"), \
                            run_file.replace("/todo/", "/doing/")
        module, func, args, kwargs = task['module'], task['function'], task['args'], task['kwargs']
        kwargs["__force_local__"] = True
        try:
                # result, logger = None, []
                exec(f"from {module} import {func}")
                # func = eval(func)
                exec("with Capturing() as self.logger: " \
                     f"    self.result = {func}(*{args}, **{kwargs})")
                # Done
                task['result'] = self.result
                task["logger"] = self.logger
                _, run_file = os.system(f"mv {run_file} {self.root}/done"), run_file.replace("/doing/", "/done/")
                json.dump(task, open(run_file, "w"), indent=4)
        except Exception as e:
            print(e)
            task["result"] = str(e)
            json.dump(task, open(run_file, "w"), indent=4)
            #Remove the operation
            os.system(f"mv {run_file} {self.root}/todo")

