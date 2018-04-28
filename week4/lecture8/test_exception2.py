while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError as e:
        print("Input not an integer; try again. -> {}!".format(e))
print("Correct input of an integer!")