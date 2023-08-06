from threading import Thread
from datetime import datetime
import time
import random
import os
from zakuro.core.remote.nodes import DirNode


class DirScanner(Thread):
    def __init__(self, root="/tmp/zakuro/dev"):
        Thread.__init__(self)
        self.root = root
        self._data = None
        self._join = False
        [os.makedirs(f"{root}/sda{k}", exist_ok=True) for k in range(9)]

    def run(self):
        while not self._join:
            dirs = [f"{self.root}/{dir}" for dir in os.listdir(self.root)]
            self._data = {
                "nodes": dirs,
                "datetime": datetime.now()
            }
            time.sleep(1)

    def pop(self):
        while self._data is None:
            time.sleep(1)
        nodes = self._data["nodes"]
        node = random.sample(nodes, 1)[0]
        return DirNode(node)

    def set_release(self):
        self._join = True
