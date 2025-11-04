def remove_char_OddIndex(str):
    new_str = ''
    for char in range(len(str)):
        if (char % 2 == 0 ):
            new_str += str[char]
    return new_str

str = 'firstbit'
res = remove_char_OddIndex(str)
print(f'original string is :{str}')
print(f'after removing odd index string is :{res}')

