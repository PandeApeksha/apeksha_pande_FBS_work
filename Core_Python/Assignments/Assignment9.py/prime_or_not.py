def is_Prime(num, i = 2):
    if (num <= 1):
        return False
    if (i == num):
        return True
    if (num % i == 0):
        return False
    return is_Prime(num, i + 1)

num = int(input('Enter a number :'))
if is_Prime(num):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')