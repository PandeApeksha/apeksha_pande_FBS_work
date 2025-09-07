beg = int(input('Enter the Beginning of range :'))
end = int(input('Enter the Ending of range :'))
divisor = int(input('Enter the Divisor :'))

for num in range(beg, end + 1):
    if (num % divisor == 0):
        print(num, end = ' ')