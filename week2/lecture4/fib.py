# -*- coding: utf-8 -*-
"""
Add caching
"""
import timeit
from timeit import Timer
from functools import lru_cache


def fibi(n):
    """
    Iterative Fibonacci
    :param n: nth number to calculate the Fibonacci value
    :return: Fibonacci value
    """

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=10000)
def fib(x):
    """assumes x an int >= 0
        returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


fib_cache = {}


def fibm(x):
    # Check cache
    if x in fib_cache:
        return fib_cache[x]

    # Compute
    if x == 0 or x == 1:
        return 1
    else:
        value = fibm(x - 1) + fibm(x - 2)
        fib_cache[x] = value
        return value


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped


wrapped = wrapper(fibm, 1000)

# for n in range(1, 10001):
#    print(n, ":", fib(n))


# create timer object

# t1 = timeit.Timer("fibm(30)")
# n = 5
# secs = t1.timeit(number=n)
# print(secs)
# print(timeit.timeit('1+3', number=100))
# print(timeit.timeit("fibm(30)", number=100))

# n = 40
# time = timeit.timeit('fib(1000)', setup='from __main__ import fib, n, fib_cache', number=n)
# time = timeit.timeit('fib(1000)', setup='from __main__ import fib, n, fib_cache', number=n)
##print(timeit.timeit(wrapped, number=5))


#t1 = Timer("fib(10)", "from __main__ import  fib")

for i in range(1, 10000):
    s = "fibm(" + str(i) + ")"
    t1 = Timer(s, "from __main__ import  fibm")
    time1 = t1.timeit(3)
    s = "fib(" + str(i) + ")"
    t2 = Timer(s, "from __main__ import  fib")
    time2 = t2.timeit(3)
    print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1 / time2))
