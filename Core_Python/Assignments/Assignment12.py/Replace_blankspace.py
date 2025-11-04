def replace_blankspace(str):
    new_str = ''
    for char in str:
        if (char == ' '):
            new_str += '-'
        else:
            new_str += char
    return new_str

str = 'Firstbit solutions Institute pune'
res = replace_blankspace(str)
print(f'original string is :{str}')
print(f'After replacing blank space with hyphen is :{res}')
