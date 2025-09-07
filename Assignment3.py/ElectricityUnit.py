Electricity_Unit = int(input('Enetr electricity units :'))

if (Electricity_Unit <= 50):
    bill = Electricity_Unit * 0.50
elif (Electricity_Unit <= 150):
    bill = (50 * 0.50) + ((Electricity_Unit - 50) * 0.75)
elif (Electricity_Unit <= 250):
    bill = (50 *0.50) + (100 * 0.75) + ((Electricity_Unit - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((Electricity_Unit - 250) * 1.50)

subcharge = bill * 0.20
total_bill = bill + subcharge

print(f'electricity bill is : {total_bill}')