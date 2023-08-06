import inspect


def get_module(func):
    file = inspect.getmodule(func).__file__
    parent_file = file.split("/zakuro/")[0]
    module = file.split(parent_file)[1].replace("/", ".").replace(".py", "")[1:]
    return module
