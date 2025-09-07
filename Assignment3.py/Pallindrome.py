num = int(input('Enter three digit number :'))

d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10

rev = d3 * 100 + d2 * 10 + d1

if (num == rev):
    print(f'{num} is a Pallindrome no.')
else:
    print(f'{num} is not a Pallindrome No.')