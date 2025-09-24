def second_Largest(li1):
    firstEle = li1[0]
    secondEle = li1[1]
    for ele in li1:
        if(ele > firstEle):
            secondEle = firstEle
            firstEle = ele
        elif(ele > secondEle and ele != firstEle):
            secondEle = ele
    return secondEle
    

li1 = [45, 23, 89, 56, 34, 77]
res = second_Largest(li1)
print(f'second largest element in the list is :{res}')