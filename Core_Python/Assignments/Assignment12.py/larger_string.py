def larger_string(str1, str2):
    len1 = 0
    len2 = 0

    for char in str1:
        len1 += 1
    for char in str2:
        len2 += 1

    if(len1 > len2):
        return 'str1 is larger.'
    elif(len2 > len1):
        return 'str2 is larger.'
    else:
        return 'both strings are same in length.'

str1 = input('Enter the str1 :')
str2 = input('Enter the str2 :')
res = larger_string(str1, str2)
print(res)