Ticket_Price = int(input('Enter Ticket Price :'))

Age1 = int(input('Enter the Age of person 1 :'))
if (Age1 < 12):
    discount1 = 30
elif (Age1 > 59):
    discount1 = 50
else:
    discount1 = 0

discount_Amt1 = Ticket_Price * discount1 / 100
amount1 = Ticket_Price - discount_Amt1

Age2 = int(input('Enter the Age of person 2 :'))
if (Age2 < 12):
    discount2 = 30
elif (Age2 > 59):
    discount2 = 50
else:
    discount2 = 0

discount_Amt2 = Ticket_Price * discount2 / 100
amount2 = Ticket_Price - discount_Amt2

Age3 = int(input('Enter the age of person 3 :'))
if (Age3 < 12):
    discount3 = 30
elif (Age3 > 59):
    discount3 = 50
else:
    discount3 = 0

discount_Amt3 = Ticket_Price * discount3 / 100
amount3 = Ticket_Price - discount_Amt3

Age4 = int(input('Enter the age of person 4 :'))
if (Age4 < 12):
    discount4 = 30
elif (Age4 > 59):
    discount4 = 50
else:
    discount4 = 0

discount_Amt4 = Ticket_Price * discount4 / 100
amount4 = Ticket_Price - discount_Amt4

Age5 = int(input('Enter the Age of person 5 :'))
if (Age5 < 12):
    discount5 = 30
elif (Age5 > 59):
    discount5 = 50
else:
    discount5 = 0

discount_Amt5 = Ticket_Price * discount5 / 100
amount5 = Ticket_Price - discount_Amt5

Total_Amt = amount1 + amount2 + amount3 + amount4 + amount5

print(f'person1 : Age :{Age1}, discount :{discount1}% {discount_Amt1}, final :{amount1}')
print(f'person1 : Age :{Age2}, discount :{discount2}% {discount_Amt2}, final :{amount2}')
print(f'person1 : Age :{Age3}, discount :{discount3}% {discount_Amt3}, final :{amount3}')
print(f'person1 : Age :{Age4}, discount :{discount4}% {discount_Amt4}, final :{amount4}')
print(f'person1 : Age :{Age5}, discount :{discount5}% {discount_Amt5}, final :{amount5}')

print(f'Total amount for all 5 People : {Total_Amt}')

