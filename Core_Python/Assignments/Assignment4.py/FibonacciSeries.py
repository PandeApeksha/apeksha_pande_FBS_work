n= int(input('How many Fibonacci snumbers you want :'))

a = -1
b = 1
c = a + b

for i in range(n):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c
    # a, b = b, c
    