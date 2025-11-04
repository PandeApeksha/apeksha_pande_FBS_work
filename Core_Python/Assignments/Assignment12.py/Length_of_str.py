def length_of_str(str):
    count = 0
    for char in str:
        count += 1

    return count

str = 'firstbit solutions'
res = length_of_str(str)
print(f'the length of string is :{res}')