CP = int(input('Enter the cost price :'))
SP = int(input('Enter the selling price :'))

if (SP > CP):
    profit = SP - CP
    profit_perc = (profit / CP) * 100
    print(f'profit : {profit}, profit in percent : {profit_perc}%')
elif (SP < CP):
    loss = CP - SP
    loss_perc = (loss / CP) * 100
    print(f'loss : {loss}, loss in percnt : {loss_perc}%')
else:
    print(f'No Profit, No Loss')
