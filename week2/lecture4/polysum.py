from math import *


def polysum(n, s):
    """
    :param n: number of sides
    :param s: length of each side
    :return: sum of : - the area and the square of the perimeter
    """
    perimeter_squared = (n * s) ** 2
    area = (0.25 * n * s ** 2) / tan(pi / n)
    return round(perimeter_squared + area, 4)


import math


def polyArea(side, length):
    area = (0.25 * side * length ** 2) / math.tan(math.pi / side)
    return area

def polyPerim(side, length):
    perim = side * length
    return perim

def polysumKN(side, length):
    results = (polyArea(side, length) + polyPerim(side, length) ** 2)
    return round(results, 4)

sum = polysum(10, 94)
