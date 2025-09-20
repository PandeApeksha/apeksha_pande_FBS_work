def digitCount(n):
    if (n == 0):
        return 0
    return 1 + digitCount(n // 10)

def sumOfPower(n, power):
    if (n == 0):
        return 0
    digit = n % 10
    return (digit ** power) + sumOfPower(n // 10, power)

def is_armstrong(num):
    power = digitCount(num)
    return num == sumOfPower(num, power)

num = int(input('Enter the number :'))
if is_armstrong(num):
    print(f'{num} is an armstrong number.')
else:
    print(f'{num} is not an armstrong number.')
    