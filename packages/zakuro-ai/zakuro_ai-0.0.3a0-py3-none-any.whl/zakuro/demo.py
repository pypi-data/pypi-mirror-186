import builtins as T
from zakuro import builtins as R
from zakuro.decorators import p2p as zakuro_p2p_function
import os

@zakuro_p2p_function
def test_remote_execution(n=10):
    for _ in range(n):
        s = T.str(f"(pid {os.getpid()}) Hello World")
        T.print(s)
    return n


@zakuro_p2p_function
def test_remote_execution_remote_object(n=10):
    for _ in range(n):
        s = R.str("Hello World")
        print(s, s())


def test_remote_object(n=10):
    for _ in range(n):
        s = R.str("Hello World")
        T.print(s)


def test_local_execution(n=10):
    for _ in range(n):
        s = T.str("Hello World")
        T.print(s)


if __name__ == "__main__":
    test_remote_execution(n=10)
    test_remote_execution_remote_object(n=10)
    test_remote_object(n=10)
    test_local_execution(n=10)
