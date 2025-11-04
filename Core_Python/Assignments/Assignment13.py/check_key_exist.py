def key_Exist(dict1, key):
    if (key in dict1):
        print('key exist in dictionary')
    else:
        print('key not exist in dictionary')

dict1 = {1: 'python', 2: 'java', 3: 'C'}
key_Exist(dict1, 2)
key_Exist(dict1, 5)