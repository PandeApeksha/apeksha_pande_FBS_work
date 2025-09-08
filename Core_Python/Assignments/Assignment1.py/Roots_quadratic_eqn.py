s = 16 ** 4


a = int(input('Enter the value of a :'))
b = int(input('Enter the value of b :'))
c = int(input('Enter the value of c :'))


Root1 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
Root2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(f'Roots of Quadratic Equation is R1 :{Root1} & R2 :{Root2}') 
