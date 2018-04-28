def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    new_dict ={}
    for k, v in d.items():
        if v in new_dict:
            mylist = new_dict[v]
            mylist.append(k)
            mylist.sort()
        else:
            new_dict[v] = [k]
    return new_dict


d = {1:10, 2:20, 3:30, 4:30}
#d = {4:True, 2:True, 0:True}
#d = {1:10, 2:20, 3:30}
value = dict_invert(d)
print(value)

#dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}