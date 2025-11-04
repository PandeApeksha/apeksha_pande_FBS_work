def replace_blankspace_hyphen(str):
    new_str = ''
    for char in str:
        if (char == ' '):
            new_str += '-'
        else:
            new_str += char
    return new_str

str = input('Enter the string :')
res = replace_blankspace_hyphen(str)
print(f'after replacing blankspace with hyphen string is :{res}')