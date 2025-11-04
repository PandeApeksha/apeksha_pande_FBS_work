def union(li1, li2):
    union_list = []
    for ele in li1:
        if (ele not in union_list):
            union_list.append(ele)
    for ele in li2:
        if (ele not in union_list):
            union_list.append(ele)
            
    return union_list


li1 = [1, 2, 3, 4, 5, 3]
li2 = [6, 7, 8, 9, 10, 8]
res = union(li1, li2)
print(f'union of two list is :{res}')