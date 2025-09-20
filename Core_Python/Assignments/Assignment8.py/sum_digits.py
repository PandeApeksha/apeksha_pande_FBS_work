def sumOfDigits(num):
    d1 = num // 100
    d2 = (num // 10) % 10
    d3 = num % 10

    sum = d1 + d2 + d3
    return sum

num = int(input('Enter the number :'))
res = sumOfDigits(num)
print(f'sum of digits of {num} is :{res}')
