Gender = input('Select the Gender (M/F):')
Age = int(input('Enetr the Age :'))

if(Gender == 'M'):
    if(Age >= 21):
        print("Eligible for Marriage")
    else:
        print("Not eligible for Marriage")
else:
    if(Age > 17):
        print("Eligible for Marriage")
    else:
        print("Not Eligible for Marriage")
