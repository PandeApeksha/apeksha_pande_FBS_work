n = int(input('Enter a Number :'))
print(f'Odd numbers upto {n} are :')

i = 1
while(i <= n):
    if (i % 2 != 0):
        print(i)
    i += 1