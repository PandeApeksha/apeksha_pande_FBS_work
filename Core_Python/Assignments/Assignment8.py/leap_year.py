def checkLeapYear(year):
    if (year % 4 == 0 or year % 100 == 0 or year % 400 == 0):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')

year = int(input('Enter the year :'))
checkLeapYear(year)