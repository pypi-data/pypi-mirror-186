from zakuro.core.remote.scanners import DirScanner
from zakuro.core.remote.schedulers import Scheduler
import json

__scanner__ = None
__scheduler__ = None

def init(scanner=DirScanner, scheduler=Scheduler):
    global __scanner__
    global __scheduler__
    __scanner__ = scanner()
    __scanner__.start()
    __scheduler__ = scheduler(__scanner__)


def exit():
    assert __scanner__ is not None
    __scanner__.set_release()
    __scanner__.join()


class RObject(str):
    def __new__(cls, data):
        global __scheduler__
        init() if __scheduler__ is None else None
        result = super(RObject, cls).__new__(cls, __scheduler__.submit(data))
        exit()
        return result

    def __call__(self, *args, **kwargs):
        return json.load(open(self, "r"))
