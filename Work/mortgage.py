# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
total_paid = 0.0
month_count = 0


while principal > 1000:
    month_count += 1
    if month_count>=extra_payment_start_month and month_count <=extra_payment_end_month:
        principal = principal * (1+rate/12) - payment-extra_payment
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(f'Month: {month_count},total_paid: {round(total_paid,2)},principal: {round(principal,2)}') 

print(f'Total paid:{round(total_paid, 2)}')
print(f'Months: {month_count}')