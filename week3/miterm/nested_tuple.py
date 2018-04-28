

master_list = []
def max_val(t):
    result = 0
    rec_result = 0

    for b in t:
        if isinstance(b, tuple) or isinstance(b, list):
            rec_result =  max_val(b)
            if rec_result > result:
                result = rec_result
        else:
            if b > result:
                result = b
            #master_list.append(b)
            #print(b)

    return result



#x = (((1, 2, 3, 4), 2, ('a', 'b', [6, 9, 7]), 6, ('$', '@')))
#x = (5, (1,2), [[1],[2]])
#x = (5, (1,2), [[1],[9]])

print(max_val((5, (1,2), [[1],[11]])))
print(max_val((5, (1,2), [[1],[9]])))
print(max_val((9, [3, 8, 2])))
print(max_val(([1, 2], [3, 4], [5, 6])))
print(max_val([[[[[[6]]]]]]))
print(max_val(([[2, 1, 5], [4, 2], 6], ([2, 1], (7, 7, 5), 6))))

x= (5, (1,2), [[1],[2]])
print("The max: {}".format(max_val(x)))
#print(master_list)