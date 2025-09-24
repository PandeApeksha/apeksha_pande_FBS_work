
a = int(input('Enter the value of a :'))
s = 0

for n in range(1,11):
    s += (a ** n) / n

print(f'the sum of series :{s}')
