def reverseNo(n):
    rev = 0
    while (n > 0):
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev

num = int(input('Enter the number :'))
res = reverseNo(num)
print(f'the reverse of {num} is :{res}')