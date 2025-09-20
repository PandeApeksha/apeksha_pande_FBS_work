def sumPower(n):
    sum = 0
    for i in range (1, n + 1):
        power = i ** i
        sum += power
    return sum

n = int(input('Enter the value of n :'))
res = sumPower(n)
print(f'sum of series 1^1+2^2+3^3+....{n}^{n} is :{res}')