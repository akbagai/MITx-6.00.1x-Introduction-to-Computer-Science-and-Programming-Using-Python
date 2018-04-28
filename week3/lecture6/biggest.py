from math import inf


def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    if len(aDict.keys()) == 0:
        return None
    max_animals = -inf

    for animals_list in aDict.values():
        if len(animals_list) >= max_animals:
            max_animals = len(animals_list)

    max_animals_list = []
    for key_value in aDict.keys():
        if len(aDict[key_value]) == max_animals:
            max_animals_list.append(key_value)

    if len(max_animals_list) == 1:
        return max_animals_list[0]
    else:
        return max_animals_list


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))


def biggest_v2(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    biggest = (None,)
    for k, v in aDict.items():
        if not all(biggest) or len(v) > biggest[1]:
            biggest = (k, len(v))
    return biggest[0]


print(biggest_v2(animals))