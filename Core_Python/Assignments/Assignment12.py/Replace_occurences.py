# text.replace('a', '$')

def replace_Occurences(str):
    new_str = ''
    for char in str:
        if (char == 'a'):
            new_str += '$'
        else:
            new_str += char
    return new_str

str = 'an apple'
res = replace_Occurences(str)
print(f'original string is :{str}')
print(f'string after a replace with $ is :{res}')