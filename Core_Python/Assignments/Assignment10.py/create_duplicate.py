def create_duplicate(li1):
    new_list = []
    for ele in li1:
        new_list.append(ele)
    return new_list

li1 =[20, 44, 32, 23, 88]
res = create_duplicate(li1)
print(f'original list is :{li1}')
print(f'duplicate list is :{res}')

dup = create_duplicate(li1)
dup[2] = 16
print(f'After modyfying duplicate list is :{dup}')