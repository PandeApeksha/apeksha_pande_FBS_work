def min_Ele(li1):
    min_num = li1[0]
    for ele in li1:
        if(ele < min_num):
            min_num = ele
    return min_num

def max_Ele(li1):
    max_num = 0
    for ele in li1:
        if(ele > max_num):
            max_num = ele
    return max_num
    
li1 = [45, 23, 89, 56, 34, 77]
res = min_Ele(li1)
res1 = max_Ele(li1)
print(f'min number in the list is :{res}')
print(f'max element in the list is :{res1}')