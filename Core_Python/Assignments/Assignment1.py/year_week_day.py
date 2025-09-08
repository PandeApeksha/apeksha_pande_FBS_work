Days = int(input('Enter the Days:'))

Years = Days // 365

Days = Days % 365

Weeks =  Days // 7

rem_Days = Days % 7

print(f'Years:{Years}, Weeks:{Weeks}, Days:{rem_Days}.')

