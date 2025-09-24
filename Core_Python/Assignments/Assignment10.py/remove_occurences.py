def remove_Occurences(li1, Element):
    new_list = []
    for ele in li1:
        if (ele != Element):
            new_list.append(ele)
    return new_list


li1 = [1, 2, 5, 3, 4, 5, 6, 7, 5]
n = int(input('Enter the element you want to remove :'))
res = remove_Occurences(li1, n)
print(f'after removing occurences of {n} is :{res}')