def sum_OF_Series(n):
    if(n == 0):
        return 0
    else:
        return n + sum_OF_Series(n - 1)
    
n = int(input('Enter the value of n :'))
res = sum_OF_Series(n)
print(f'the sum of series is :{res}')