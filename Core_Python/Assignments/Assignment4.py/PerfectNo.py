num = int(input('Enter the Number :'))
i = 1
sum = 0

while (i < num):
    if (num % i == 0):
        sum += i
    i += 1

if (sum == num):
    print(f'{num} is a Perfect number.')
else:
    print(f'{num} is not a Perfect number.')