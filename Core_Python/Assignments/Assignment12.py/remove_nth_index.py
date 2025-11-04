def remove_nth_index(str):
    new_str = ''
    for i in range(len(str)):
        if (i != n):
            new_str = new_str + str[i]

    return new_str

str = 'Firstbit'
n = 2
res = remove_nth_index(str)
print(f'string after removing nth index :{res}')