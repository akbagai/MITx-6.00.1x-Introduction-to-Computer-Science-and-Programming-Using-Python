print("Should pass:")
x = 7
y = x**2
print("x = {}".format(x))
print("y = {}".format(y))
assert y >= 0

'''''
print("Should fail!")
print("Assertion error:")
x = 2*1j
y = x**2
print("x = {}".format(x))
print("y = {}".format(y))
assert y >= 0
'''''

print("Done!")


# Simple unit test
def square_me(x):
    return x**2

# Should all pass
assert square_me(0) == 0
assert square_me(2) == 4
assert square_me(3) == 9

# Should fail, bug in function
# Simple unit test
def square_me(x):
    return -x**2

print("Assertion should fail due to bug in func square_me")
assert square_me(0) == 0
assert square_me(2) == 4
assert square_me(3) == 9