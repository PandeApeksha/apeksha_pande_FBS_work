a = int(input('Enter first Angle :'))
b = int(input('Enter second Angle :'))
c = int(input('Enter third Angle :'))

if (a + b + c == 180):
    if (a == b == c):
        print("The triangle is Equilateral.")
    elif (a == b) or (b == c) or (a == c):
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("It is not valid triangle.")