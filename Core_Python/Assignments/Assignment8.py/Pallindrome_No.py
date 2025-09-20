def pallindromeNo(n):
    rev = 0
    while (n > 0):
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return num == rev

num = int(input('Enter the number :'))
if pallindromeNo(num):
    print(f'{num} is a pallindrome number.')
else:
    print(f'{num} is not a pallindrome number.')