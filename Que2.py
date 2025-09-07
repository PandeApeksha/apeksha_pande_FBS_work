num = int(input('Enter a three digit number :'))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

print(f'd1 :{d1}, d2 :{d2}, d3 :{d3}')

if (d3 ==  2 * d2) and (d3 == d1 / 2):
    print("yes, you have done it.")
else:
    print("Please try Next Time.")