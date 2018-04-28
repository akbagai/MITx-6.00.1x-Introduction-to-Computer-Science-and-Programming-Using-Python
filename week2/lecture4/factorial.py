from functools import reduce

def factorial_iter(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)


def factorial_reduce(n):
    return reduce(lambda x, y: x * y, [1] + list(range(1, n + 1)))



for i in range(10):
    print("     factorial_iter({}) = {}".format(i, factorial_iter(i)))
    print("factorial_recursive({}) = {}".format(i, factorial_recursive(i)))
    print("   factorial_reduce({}) = {}".format(i, factorial_reduce(i)))
    print("--------------------------------")
