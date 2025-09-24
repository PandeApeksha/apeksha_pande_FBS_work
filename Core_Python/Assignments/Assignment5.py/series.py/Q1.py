n = int(input('Enter the value of n :'))
sum = 0

for i in range(n + 1):
    sum += 2 ** i

print(f'sum is :{sum}')
