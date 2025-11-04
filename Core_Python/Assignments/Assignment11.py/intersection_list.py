def intersection(li1, li2):
    intersection_list = []
    for ele in li1:
        if (ele in li2 and ele not in intersection_list):
            intersection_list.append(ele)
    
    return intersection_list

li1 = [1, 2, 3, 4, 5, 6]
li2 = [2, 10, 5, 15, 20]
res = intersection(li1, li2)
print(f'intersection of two list is :{res}')
