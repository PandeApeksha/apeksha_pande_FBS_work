def count_letter_digit(str):
    letter_count = 0
    digit_count = 0
    for char in str:
        if('a' <= char <= 'z' or 'A' <= char <='Z'):
            letter_count += 1
        elif('0' <= char <= '9'):
            digit_count += 1

    return letter_count, digit_count

str = 'FirstBit Solutions 123'
letter, digit = count_letter_digit(str)
print(f'letters in the string is :{letter}')
print(f'digits in the string is :{digit}')


