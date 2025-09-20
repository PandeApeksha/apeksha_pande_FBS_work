def reverse_Num(n, rev = 0):
    if (n == 0):
        return rev
    rev = rev * 10 + (n % 10)
    return reverse_Num(n // 10, rev)

num = int(input('Enter a number :'))
res = reverse_Num(num)
print(f'reversed number of {num} is {res}')