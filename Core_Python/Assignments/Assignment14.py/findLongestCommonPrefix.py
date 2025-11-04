def longest_common_prefix(words):
    prefix = ''
    if not words:
        return prefix
    
    first_word = min(words, key = len)

    for i in range(len(first_word)):
        chars = set()

        for w in words:
            chars.add(w[i])
        
        if (len(chars) == 1):
            prefix += first_word[i]
        else:
            break

    return prefix

words = ["flower", "flow", "flight"]
res = longest_common_prefix(words)
print(f'longest common prefix is :{res}')