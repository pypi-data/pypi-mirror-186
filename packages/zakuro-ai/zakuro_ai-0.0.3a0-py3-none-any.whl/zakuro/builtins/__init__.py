from builtins import print as __print__
from builtins import int as __int__
from builtins import float as __float__
from builtins import str as __str__
from builtins import dict as __dict__
from zakuro.core.remote import RObject

def int(data):
    assert type(data) == __int__
    return RObject(data)

def float(data):
    assert type(data) == __float__
    return RObject(data)

def str(data):
    assert type(data) == __str__
    return RObject(data)

def dict(data):
    assert type(data) == __dict__
    return RObject(data)

def print(robject):
    return __print__(robject())