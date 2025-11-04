def add_Pair(dict1, key, value):
    dict1.update({key: value})
    return dict1

dict1 = {1: 'python', 2: 'java', 3: 'C'}
res = add_Pair(dict1, 4, 'Ruby')
print(f'updated Dictionary : {res}')
