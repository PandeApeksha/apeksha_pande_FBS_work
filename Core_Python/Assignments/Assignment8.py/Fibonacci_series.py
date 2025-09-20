def fibonacciSeries(n):
    a = -1
    b = 1
    for i in range(n):
        c = a + b
        print(c, end = ' ')
        a = b
        b = c

n = int(input('how many fibonacci numbers you want :'))
fibonacciSeries(n)

