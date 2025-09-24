def sum_list(li):
    sum = 0
    for ele in li:
        sum += ele
    return sum

li = [10, 20, 30]
result = sum_list(li)
print("Addition is:", result)
