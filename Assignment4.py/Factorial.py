num = int(input('Enter the Number :'))

i = 1
fact = 1
while (i <= num):
    fact = fact * i
    i += 1

print(f'The Factorial of {num} is :{fact}')