def sumOddNo(beg, end):
    sum = 0
    for i in range(beg, end + 1):
        if (i % 2 != 0):
            sum += i
    return sum
        
beg =int(input('Enter the beginning of range :'))
end = int(input('Enter the ending of range :'))

res = sumOddNo(beg, end)
print(f'sum of all odd numbers between {beg} to {end} is :{res}')