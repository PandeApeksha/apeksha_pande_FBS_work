def fact(num):
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f

def sumFact(n):
    sum = 0
    for i in range(1, n + 1):
        sum += fact(i)
    return sum

n = int(input('Enter a value of n :'))
res = sumFact(n)
print(f'sum of factorial from 1! to {n}! is :{res}')


