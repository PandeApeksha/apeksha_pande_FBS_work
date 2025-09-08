n = int(input('Enter a Number :'))
print(f'intergers upto {n} are not divisible by 2 and 3')

i = 1
while(i <= n):
    if (i % 2 != 0 and i % 3 != 0):
        print(i)
    i += 1