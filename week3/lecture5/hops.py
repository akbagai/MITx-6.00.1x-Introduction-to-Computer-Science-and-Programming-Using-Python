"""
HOPS - Higher order procedure

General purpose HOP: map

@author: bagai
"""

val = map(abs, [1, -2, 3, -4])

for i in val:
    print(i)



def applyToEach(L, f):
    """assumes L is a list, fa function
    mutates L by replacing each element,
    e, of L by f(e)"""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1,-2, 3, 3.4]

applyToEach(L, abs)
print(L)
applyToEach(L, int)
print(L)


