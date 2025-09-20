def sum_Prime(n):
    sum = 0
    for i in range(2, n + 1):
        prime = True
        for j in range(2, i):
            if (i % j == 0):
                prime = False
                break
        if prime:
            sum = sum + i
    return sum

n = int(input('Enter the value of n :'))
res = sum_Prime(n)
print(f'sum of prime numbers between 1 to {n} is :{res}')