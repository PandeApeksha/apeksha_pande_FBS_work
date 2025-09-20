def sum_Digit(num):
    if (num == 0):
        return 0
    return(num % 10) + sum_Digit(num // 10)

n = int(input('Enter a number :'))
res = sum_Digit(n)
print(f'sum of digits is :{res}')