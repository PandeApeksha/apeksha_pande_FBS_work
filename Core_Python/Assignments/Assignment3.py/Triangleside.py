a = int(input('Enter first side :'))
b = int(input('Enter second side :'))
c = int(input('Enter third side :'))

if (a + b > c) and (a + c > b) and (b + c > a):

    print("It is a valid Triangle.")
else:
    print("It is not a valid Triangle.")