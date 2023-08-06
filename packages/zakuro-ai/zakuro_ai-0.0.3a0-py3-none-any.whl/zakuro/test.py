from functools import wraps

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


def decorator(timeout=None):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print("Arguements passed to decorator %s" % (timeout))
            result = function(*args, **kwargs)
            return result
        return wrapper
    return inner_function


# @decorator
# def print_args(*args):
#     for arg in args:
#         print(arg)


# print_args(1, 2, 3)


@decorator(timeout=1)
def do_something(s):
    print(s)

stdout = None
func = "do_something"
exec("with Capturing() as stdout: "  \
     f"    {func}('hello world')")
print(stdout)
do_something('hello world')