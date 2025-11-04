def count_LowercaseChar(str):
    count = 0
    for char in str:
        if ('a' <= char <= 'z'):
            count += 1
    return count

str = 'FirstBit Solutions'
res = count_LowercaseChar(str)
print(f'lowercase characters in the string is :{res}')
        
