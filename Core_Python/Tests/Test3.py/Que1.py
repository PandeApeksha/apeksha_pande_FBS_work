n = int(input('How many numbers you want print :'))
print(f'{n} prime numbers are :')

count = 0
num = 2

while(count < n):
    for i in range(2, num):
        if (num % i == 0):
            break
    else:
        print(num)
        count += 1
    num += 1