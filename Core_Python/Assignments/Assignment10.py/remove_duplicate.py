def remove_Duplicate(li1):
    new_list = []
    for ele in li1:
        if (ele not in new_list):
            new_list.append(ele)
    return new_list

li1 = [10, 20, 30, 40, 50, 30, 20]
print(f'original list :{li1}')
res = remove_Duplicate(li1)
print(f'list after removing duplicates :{res}')


