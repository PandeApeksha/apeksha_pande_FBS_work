def calculate_No_words_chars(str1):
    char_count = 0
    word_count = 1
    for char in str1:
        char_count += 1
        if (char == ' '):
            word_count += 1

    return char_count, word_count 

str1 = 'firstbit solutions institute pune'
char, word = calculate_No_words_chars(str1)
print(f'number of characters in the string is :{char}')
print(f'number of words in the string is :{word}')