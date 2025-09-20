def fact(n):
    f = 1
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)

   
n = int(input('Enter the number :'))
res = fact(n)
print(f'factorial of {n} is : {res}')