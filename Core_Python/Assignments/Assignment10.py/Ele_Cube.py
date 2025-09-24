def cube_of_Number(li):
    new_list = []
    cube = 0
    for ele in li1:
        cube = ele ** 3
        new_list.append(cube)
    return new_list
        

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = cube_of_Number(li1)
print(res)