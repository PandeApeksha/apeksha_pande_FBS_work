def divisible_By_Num(li1):
    m = 3
    n = 5
    new_list = []
    for ele in li1:
        if (ele % m == 0):
            new_list.append(ele)
        elif (ele % n == 0):
            new_list.append(ele)
    return new_list


li1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
res = divisible_By_Num(li1)
print(f'numbers which are divisible by m and n are :{res}')