aList = ["apple", "cat", "dog", "banana", "dogg"]


def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    new_list = []
    for item in aList:
        if (len(item)) < 4:
            new_list.append(item)

    return new_list


value = lessThan4(aList)