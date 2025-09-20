def sum(n):
    sum = 0
    for i in range (1, n + 1):
        sum += i
    return sum

n = int(input('Enter the value of n :'))
res = sum(n)
print(f'sum of numbers from 1 to {n} is :{res}')
