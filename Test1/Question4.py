
total_area = int(input("Enter area of one wall: "))
interior_cost = int(input("Enter interior  cost  area: "))
exterior_cost = int(input("Enter exterior  cost area: "))



interior_cost = total_area * interior_cost
exterior_cost = total_area * exterior_cost
total_cost = interior_cost + exterior_cost

print(f'Interior cost : {interior_cost} , Exterior cost : {exterior_cost} Total painting cost: {total_cost}')