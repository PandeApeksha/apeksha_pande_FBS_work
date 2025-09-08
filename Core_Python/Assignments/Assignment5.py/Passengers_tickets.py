passengers = int(input('Enter the number of passengers :'))
ticket_cost = int(input('Enter ticket cost per passenger:'))
total_amount = 0

for i in range(1, passengers + 1):
    Age = int(input(f'Enter the age of passenger {i} :'))
    if (Age < 12):
        discount = 30
    elif (Age > 59):
        discount = 50
    else:
        discount = 0
    
    discount_Amt = ticket_cost * discount / 100
    amount = ticket_cost - discount_Amt

    print(f'Ticket Amount for Passenger {i} (Age {Age}) is :{amount}')
    total_amount = total_amount + amount

print(f'total Amount to be paid : {total_amount}')