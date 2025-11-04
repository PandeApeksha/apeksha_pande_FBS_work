def count_frequency(s):
    d = {}
    word = ''
    i = 0

    while (i < len(s)):
        if (s[i] != ' '):
            word = word + s[i]
        else:
            if (word != ''):
                if (word in d):
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
                word = ''
        i = i + 1

    if (word != ''):
        if (word in d):
            d[word] = d[word] + 1
        else:
            d[word] = 1
    
    return d

string = input("Enter a string :")
res = count_frequency(string)
print(f'word frequency :{res}')