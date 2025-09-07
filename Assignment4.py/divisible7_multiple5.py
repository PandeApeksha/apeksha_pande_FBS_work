beg = int(input('Enter the Beginning of Range:'))
end = int(input('Enter the Ending of Range :'))

for num in range(beg, end + 1):
    if (num % 7 == 0 and num % 5 == 0):
        print(num, end = ' ')
        
