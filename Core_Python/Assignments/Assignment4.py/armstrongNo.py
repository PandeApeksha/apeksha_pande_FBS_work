beg = int(input('Enter the beginning of range: '))
end = int(input('Enter the ending of range: '))

for num in range(beg, end + 1):
    n = num
    temp = num
    count = 0

    while temp > 0:
        temp = temp // 10
        count += 1

    temp = num
    sum_of_power = 0

    while temp > 0:
        digit = temp % 10
        power = 1
        for i in range(count):
            power = power * digit
        sum_of_power = sum_of_power + power
        temp = temp // 10

    if sum_of_power == n:
        print(n)
