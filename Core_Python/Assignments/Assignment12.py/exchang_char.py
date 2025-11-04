def exchange_char(str):
    new_str = ''
    for char in range(len(str)):
        if (char == 0):
            new_str += str[-1]
        elif (char == len(str) - 1):
            new_str += str[0]
        else:
            new_str += str[char]
    return new_str

str = 'Firstbit Solutions'
res = exchange_char(str)
print(f'original string is :{str}')
print(f'new string is :{res}')
        