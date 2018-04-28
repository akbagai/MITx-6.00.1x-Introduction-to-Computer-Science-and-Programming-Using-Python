balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
runBalance = balance
unpaid_balance = balance

lowest_payment = balance / 12
highest_payment = (balance * (1 + monthlyInterestRate) ** 12) / 12

epsilon = 0.01
not_found_payment_rate = True
count = 0

while not_found_payment_rate:
    payment = (lowest_payment + highest_payment) / 2
    runBalance = balance
    unpaid_balance = balance

    for month in range(0, 12):
        count += 1
        unpaid_balance = runBalance - payment
        interest = unpaid_balance * monthlyInterestRate
        runBalance = unpaid_balance + interest

        if abs(unpaid_balance) <= epsilon:
            not_found_payment_rate = False
            break

        if unpaid_balance < 0 and abs(unpaid_balance) > epsilon:
            highest_payment = payment  # paying too much, should pay less
            break

    if unpaid_balance > 0 and abs(unpaid_balance) > epsilon:
        lowest_payment = payment  # paying too little, should pay more

print(count)
payment = round(payment, 2)
print("Lowest Payment: {}".format(payment))
