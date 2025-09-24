
def square_Cube(li1):
    square = 0
    cube = 0
    square_list = []
    cube_list = []
    for ele in li1:
        square = ele * ele
        square_list.append(square)
        cube = ele ** 3
        cube_list.append(cube)
    return square_list, cube_list
        

n = int(input('How many numbers you want to add in the list :'))
li1 = []
for i in range(n):
    num = int(input(f'Enter the element :'))
    li1.append(num)

square, cube = square_Cube(li1)

print(f'numbers of list :{li1}')
print(f'squares of list :{square}')
print(f'cube of list :{cube}')
