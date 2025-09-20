def fibo_Series(n, a, b):
    if (n > 0):
        c = a + b
        print(c, end= ' ')
        fibo_Series(n - 1, b, c)

n = int(input('how many fibonacci numbers you want :'))
res = fibo_Series(n, -1, 1)
