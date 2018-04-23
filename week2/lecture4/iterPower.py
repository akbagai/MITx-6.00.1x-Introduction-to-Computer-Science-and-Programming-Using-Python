def iter_power(base, exp):
    """
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    """
    total = 1.0000
    for i in range(1, exp + 1):
        total *= base

    return total


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    negative = False
    if base < 0 and (exp % 2 == 1):
        negative = True

    base = abs(base)
    result = 1

    if exp <= 0:
        return 1
    elif exp == 1:
        result = base
    else:
        for i in range(exp):
            result = result * base

    if negative:
        result = -1 * result

    return result


print(iter_power(-7.83, 5))
print(iterPower(-7.83, 5))



