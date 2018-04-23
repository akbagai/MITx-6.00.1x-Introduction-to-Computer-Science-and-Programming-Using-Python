# -*- coding: utf-8 -*-
"""
Add caching
"""
import timeit
from functools import lru_cache


#@lru_cache(maxsize=10000)
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

wrapped = wrapper(fibm, 30)


# for n in range(1, 10001):
#    print(n, ":", fib(n))


# create timer object

# t1 = timeit.Timer("fibm(30)")
# n = 5
# secs = t1.timeit(number=n)
# print(secs)
# print(timeit.timeit('1+3', number=100))
# print(timeit.timeit("fibm(30)", number=100))

#n = 40
# time = timeit.timeit('fib(1000)', setup='from __main__ import fib, n, fib_cache', number=n)
#time = timeit.timeit('fib(1000)', setup='from __main__ import fib, n, fib_cache', number=n)
print(timeit.timeit(wrapped, number=5))
