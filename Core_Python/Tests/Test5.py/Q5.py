def list_union(list1, list2):
    union_list = list1.copy()

    for item in list2:
        if item not in union_list:  
            union_list.append(item)
    return union_list
    
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print("List 1 :",list1)
print("List 2 :",list2)

result = list_union(list1, list2)
print("Union of the two lists :" ,result)