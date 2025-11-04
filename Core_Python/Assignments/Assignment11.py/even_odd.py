def Even_Odd(li1):
    Even_list = []
    Odd_list = []
    for ele in li1:
        if (ele % 2 == 0):
            Even_list.append(ele)
        else:
            Odd_list.append(ele)
    return Even_list, Odd_list

li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even, Odd = Even_Odd(li1)
print(f'Even numbers of list is :{Even}')
print(f'Odd numbers of list is :{Odd}')