def unique_word_frequency(worldList):
    unique_words = set(worldList)
    for word in unique_words:
        count = 0
        for w in worldList:
            if w == word:
                count += 1
        print(f'{word} : {count}')

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi']
unique_word_frequency(words)
