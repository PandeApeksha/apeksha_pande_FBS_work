def multiply_Items(dict1):
    mul = 1
    for value in dict1.values():
        mul *= value
    return mul

dict1 = {'a': 10, 'b': 20, 'c': 30}
res = multiply_Items(dict1)
print(f'multiply of all items is :{res}')