year = int(input('Enter the year :'))

if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f'{year} is a Leap year.')
        print(f'{year} is a Leap year.')
    print(f'{year} is a Leap year.')
else:
    print(f'{year} is not a Leap year.')