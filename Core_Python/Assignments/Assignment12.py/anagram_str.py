def is_Anagram(str1, str2):
    if(len(str1) == len(str2)):
        di = {}
        for i, j in zip(str1, str2):
            if i in di:
                di[i] = di[i] + 1
            else:
                di[i] = 1

            if j in di:
                di[j] = di[j] - 1
            else:
                di[j] = -1

        for val in di.values():
            if(val != 0):
                print("strings are not anagram.")
                break
        else:
            print("strings are anagrams.")
    else:
        print("strings are not anagrams.")
        
    return 

str1 = 'abcca'
str2 = 'bacad'
res = is_Anagram(str1, str2)
print(res)