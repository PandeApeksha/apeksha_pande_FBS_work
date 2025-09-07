num = int(input('Enter the Number :'))
temp = num
sum = 0
digits = 0
count = num

while(count > 0):
    digits += 1
    count //= 10

while(temp > 0):
    rem_num = temp % 10
    sum += rem_num ** digits
    temp //= 10

if (num == sum):
    print(f'{num} is an Armstrong number.')
else:
    print(f'{num} is not an Armstrong number.')