balance = 3926
annualInterestRate = 0.2

rate = annualInterestRate / 12.0
payment = 10

while True:
    previous_balance = balance
    for idx in range(1, 13):
        monthly_unpaid_balance = balance - payment
        balance = monthly_unpaid_balance + rate * monthly_unpaid_balance
    if balance < 0:
        break
    payment += 10
    balance = previous_balance

print("Lowest Payment: " + str(round(payment, 2)))


##############################
balance = 4773
annualInterestRate = 0.2

import math


def roundup(x):
    return int(math.floor(x / 10.0)) * 10


monthlyInterestRate = annualInterestRate / 12
runBalance = balance
unpaid_balance = balance

lowest_payment = roundup(balance / 12)
increament_payment = 10
not_found_payment_rate = True

while not_found_payment_rate:

    lowest_payment = lowest_payment + increament_payment
    runBalance = balance
    unpaid_balance = balance

    for month in range(0, 12):

        this_month_payment = lowest_payment
        unpaid_balance = runBalance - this_month_payment
        interest = unpaid_balance * monthlyInterestRate
        runBalance = unpaid_balance + interest

        if unpaid_balance < 0:
            not_found_payment_rate = False
            break

lowest_payment = round(lowest_payment, 2)
print("Lowest Payment: {}".format(lowest_payment))