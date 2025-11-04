def find_Element(set1, set2):
    new_set = set()
    for ele in set1:
        if (ele not in set2):
            new_set.add(ele)
    return new_set

set1 = {10, 13, 15, 18}
set2 = {11, 15, 14, 19}
res = find_Element(set1, set2)
print(f'elements in a not in b is :{res}')
