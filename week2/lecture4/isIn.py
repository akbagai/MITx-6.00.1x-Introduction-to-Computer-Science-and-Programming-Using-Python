def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) == 0:
        return False

    if len(aStr) == 1:
        return char == aStr[0]

    if aStr[int(len(aStr) / 2)] == char:
        return True

    if char < aStr[int(len(aStr) / 2)]:
        return isIn(char, aStr[:int(len(aStr) / 2)])
    else:
        return isIn(char, aStr[int(len(aStr) / 2):])


import math


# print(math.ceil(4.2))

def isInKN(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''

    # base
    if len(aStr) == 0:
        return False
    if len(aStr) == 1 and char == aStr[0]:
        return True
    if len(aStr) == 1 and char != aStr[0]:
        return False

    strLen = len(aStr)
    index = int(math.floor(len(aStr) / 2))
    sel_char = aStr[index]
    if char == sel_char:
        return True

    # recursive
    if char < sel_char:
        return isIn(char, aStr[0:index])
    else:
        return isIn(char, aStr[index:])
