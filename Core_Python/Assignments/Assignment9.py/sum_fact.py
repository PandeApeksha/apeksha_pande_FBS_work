def fact(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * fact(num - 1)
    
def sum_Fact(n):
    if (n == 1):
        return 1
    else:
        return fact(n) + sum_Fact(n - 1)
    
n = int(input('Enter a number :'))
res = sum_Fact(n)
print(f'sum of series :{res}')

    
