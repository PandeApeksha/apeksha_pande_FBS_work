def max_min(li):
    max_num = li[0]
    min_num = li[0]
    
    for ele in li:
        if ele > max_num:
            max_num = ele
        if ele < min_num:
            min_num = ele
    
    return max_num, min_num


li = [50,60,70,90]
max_num, min_num = max_min(li)
print("Max number:", max_num)
print("Min number:", min_num)
