Principle_amt = int(input('Enter the Principle amt:'))
rate = int(input('Enter the rate:'))
time = int(input('Enter the time:'))

Compound_Interest = Principle_amt * ((1 + rate/100)** time) - Principle_amt

print(f'Compound interest is:{Compound_Interest}')