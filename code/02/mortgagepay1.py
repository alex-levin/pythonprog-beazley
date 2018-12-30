principal = 27000
payment = 200
rate = 5
total_payments = 0

while principal > 0:
    interest = principal * rate / 100 / 12
    principal = principal + interest - payment
    total_payments = total_payments + payment

print('Total payments:', total_payments)
