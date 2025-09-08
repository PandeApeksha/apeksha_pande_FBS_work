num = int(input('Enter three digit number :'))

d1 = num // 100

d2 = (num // 10) % 10

d3 = num % 10

print(f'Digits are : d1:{d1}, d2:{d2}, d3:{d3}')

rev_No = d3 * 100 + d2 * 10 + d1 

print(f'The reverse number of {num} is :{rev_No}')


