
n = int(input('Enter the value of n :'))
total = 0

for i in range(1, n + 1):
    total = total + n ** i

print(f'the sum of the series N+N^2+N^3+N^4...+N^N is :a ={total}')
