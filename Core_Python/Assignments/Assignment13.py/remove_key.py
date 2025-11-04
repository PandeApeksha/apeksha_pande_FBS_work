def remove_key(dict1):
    dict1.pop(2)
    return dict1

dict1 = {1: 'python', 2: 'java', 3: 'C'}
res = remove_key(dict1)
print(f'after removing key dictionary is :{res}')