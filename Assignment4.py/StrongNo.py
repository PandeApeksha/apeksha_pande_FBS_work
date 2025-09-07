num = int(input('Enter the Number :'))
temp = num
sum = 0

while (temp > 0):
    rem_num = temp % 10
    fact = 1
    i = 1

    while (i <= rem_num):
        fact = fact * i
        i += 1
    sum += fact
    temp = temp // 10

if (num == sum):
    print(f'{num} is a strong number.')
else:
    print(f'{num} is not a strong number.')
    

