area = int(input('Enter the Area of one wall :'))
Ci = int(input('Enter the cost of interior wall per unit area:'))
Ce = int(input('Enter the cost of exterior wall per unit area :'))

interior_Area = 8 * area
exterior_Area = 7 * area

interior_cost = interior_Area * Ci
exterior_cost = exterior_Area * Ce

Total_cost = (interior_cost + exterior_cost)


print(f'cost of painting the building wall is : {Total_cost} ')