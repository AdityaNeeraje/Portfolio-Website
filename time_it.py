from time import time

def timeit(func):
    start = time()
    func()
    end = time()
    a = end - start
    int_a = int(a)
    a -= int_a
    b = (10**3)*a
    int_b = int(b)
    b -= int_b
    c = (10**3)*b
    int_c = int(c)
    c -= int_c
    d = (10**3)*c
    int_d = int(d)
    print(f"{func.__name__} has a run time of {int_a} seconds, {int_b} milliseconds, {int_c} microseconds and {int_d} nanoseconds.")


def func():
    for i in range(1000000):
        a = i**20

timeit(func)