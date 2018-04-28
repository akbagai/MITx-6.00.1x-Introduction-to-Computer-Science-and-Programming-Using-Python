try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a/b)
    print("a+b= ", a+b)
except ValueError as e:
    print("Could not convert to a number. ", e)
except ZeroDivisionError as e:
    print("Can't divide by zero! ", e)
except:
    print("Something went very wrong.")

print("outside!")