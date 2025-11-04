def merge_Sort(li1, li2):
    merged_list = li1 + li2
    merged_list.sort()
    return merged_list


li1 = [10, 20, 30, 40, 50]
li2 = [5, 15, 25, 35, 45]
res = merge_Sort(li1, li2)
print(f'Merge and Sorted list is :{res}')