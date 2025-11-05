def palindrome_generator():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1

pal_gen = palindrome_generator()

print("First 20 palindrome numbers:")
for _ in range(20):
    print(next(pal_gen), end=" ")
