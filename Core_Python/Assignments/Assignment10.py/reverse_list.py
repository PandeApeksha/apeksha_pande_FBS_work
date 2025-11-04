def reverse(li1):
    for ele in li1:
        start = 0
        end = len(li1) - 1

        while (end > start):
            li1[start], li1[end] = li1[end], li1[start]
            start = start + 1
            end = end - 1
    return li1

li1 = [10, 20, 30, 40, 50]
res = reverse(li1)
print(f'The reversed list is :{res}')



