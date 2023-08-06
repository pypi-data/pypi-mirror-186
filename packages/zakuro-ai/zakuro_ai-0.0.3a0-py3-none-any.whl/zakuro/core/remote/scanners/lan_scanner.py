import nmap
from threading import Thread
from datetime import datetime
from gnutools.fs import listfiles, parent
from gnutools.utils import id_generator
import time
import random
import json
import os


class LanScanner(Thread):
    def __init__(self, group="192.168.1.0"):
        Thread.__init__(self)
        self.group = group
        self._data = None

    def run(self):
        nm = nmap.PortScanner()
        while True:
            hosts = nm.scan(hosts=f"{self.group}/24", arguments="-sP")
            self._data = {
                "nodes": list(hosts["scan"].keys()),
                "datetime": datetime.now(),
            }

            time.sleep(1)
