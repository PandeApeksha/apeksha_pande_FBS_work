sec = int(input('Enter the time in second :'))

Hrs = sec // 3600

rem_sec = sec - 3600

min = rem_sec // 60

sec = rem_sec % 60

print(f'Hours:{Hrs}h, minutes:{min}min, second:{sec}sec')

