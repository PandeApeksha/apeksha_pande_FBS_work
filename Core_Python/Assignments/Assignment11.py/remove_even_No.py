def remove_Even_No(li1):
    new_list = []
    for ele in li1:
        if (ele % 2 != 0):
            new_list.append(ele)
    return new_list

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = remove_Even_No(li1)
print(f'after removing even numbers list is :{res}')