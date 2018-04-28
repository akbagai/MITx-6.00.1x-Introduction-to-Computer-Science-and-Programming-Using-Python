def count7(N):
    N = abs(N)
    right_digit = N % 10
    base = N // 10

    if base == 0 and right_digit == 7:
        return 1
    elif base == 0:
        return 0
    else:
        return count7(base) + count7(right_digit)


print(count7(17700700077737777))