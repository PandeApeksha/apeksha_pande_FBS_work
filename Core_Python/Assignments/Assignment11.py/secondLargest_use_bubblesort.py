def bubbleSort(li):
    for i in range(1, len(li)):
        for j in range(0, len(li) - 1):
            if (li[j] > li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]
            
    return li

def second_largest(li):
    sorted_list = bubbleSort(li)
    return sorted_list[-2]

numbers = [12, 45, 23, 67, 34, 89, 10]
print(f'original list :{numbers}')
res = second_largest(numbers)
print(f'Second largest number is :{res}')
