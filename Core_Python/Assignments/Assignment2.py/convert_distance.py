feet = int(input('Enter the distance in feet :'))
inch = int(input('Enter the distance in inch :'))

Total_inches = feet * 12 + inch #convert feet into inch

centimeter = Total_inches * 2.54 # convert inch into centimeter

meter = centimeter/100 # convert centimeter into meter

rem_centimeter = centimeter % 100 

print(f'the distance in meter is :{meter}m and centimeter is :{rem_centimeter}cm')

