def remove_Even_No(li1):
    new_list = []
    for ele in li1:
        if (ele % 2 != 0):
            new_list.append(ele)
    return new_list

li1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
res = remove_Even_No(li1)
print(f'after removing even numbers list is :{res}')