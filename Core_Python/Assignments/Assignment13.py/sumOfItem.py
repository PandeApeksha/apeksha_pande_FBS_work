def sum_Items(dict1):
    return sum(dict1.values())

dict1 = {'a': 100, 'b': 200, 'c': 300}
res = sum_Items(dict1)
print(f'sum of all items is :{res}')