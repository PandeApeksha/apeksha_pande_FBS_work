def findMissingNo(li1, li2):
    missing_in_2 = []
    missing_in_1 = []

    for num in li1:
        found = False
        for n in li2:
            if num == n:
                found = True
                break
        if not found:
            missing_in_2.append(num)

    for num in li2:
        found = False
        for n in li1:
            if num == n:
                found = True
                break
        if not found:
            missing_in_1.append(num)
    
    return missing_in_2, missing_in_1 

li1 = [1, 2, 3, 4, 5]
li2 = [2, 3, 6]

missing_in_2, missing_in_1 = findMissingNo(li1, li2)

print(f'No. in li1 but missing in li2 :{missing_in_2}')
print(f'No. in li2 but missing in li1 :{missing_in_1}')

