def count_Occurences(str1):
    words = []
    word = ''
    for char in str1:
        if (char != ' '):
            word += char
        else:
            if (word != ' '):
                words.append(word)
                word = ''
    if (word != ''):
        words.append(word)

    for w in words:
        count = 0
        for x in words:
            if (x == w):
                count += 1
        print(w, count)

str1 = 'python is easy language and python easy to understand'
count_Occurences(str1)
