def count_Vowels(str):
    count = 0
    for char in str:
        if(char in 'aeiouAEIOU'):
            count += 1

    return count

str = 'Kamini'
res = count_Vowels(str)
print(f'vowels in the string is :{res}')
