def concatenate(dict1, dict2):
    dict1.update(dict2)
    return dict1

dict1 = {1: 'python', 2: 'java'}
dict2 = {3: 'Ruby', 4: 'React'}
res = concatenate(dict1.copy(), dict2)
print(f'concatenate dictionary is :{res}')