from contextlib import contextmanager
from time import perf_counter


def fac(num):
    assert num > 0
    if num in (0,1):
        return 1
    return num * fac(num - 1)

def fib(num):
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a + b
    
    return a

def fib2(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a
