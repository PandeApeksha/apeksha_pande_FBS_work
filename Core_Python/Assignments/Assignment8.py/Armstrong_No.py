def digitCount(num):
    cnt = 0
    while(num!=0):
        num = num // 10
        cnt += 1

    return cnt

def sum_of_pow(num, cnt):
    sum = 0
    while(num!= 0):
        rem = num % 10
        sum = sum + (rem ** cnt)
        num = num // 10

    return sum

def is_armstrong(num):        #calling function
    cnt = digitCount(num)     #called function
    sum = sum_of_pow(num, cnt)
    if (sum == num):
        print(f'{num} is a armstrong number.')
    else:
        print(f'{num} is not a armstrong number.') 

num = int(input('Enter the number :'))   
is_armstrong(num)























        