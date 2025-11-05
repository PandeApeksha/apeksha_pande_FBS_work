sentence = input("Enter a sentence: ")

word_lengths = {word: len(word) for word in sentence.split()}

print("Word lengths:", word_lengths)
