text = input("Enter a string: ")

vowels = "aeiouAEIOU"

result = ''.join([ch for ch in text if ch not in vowels])

print("String after removing vowels:", result)
