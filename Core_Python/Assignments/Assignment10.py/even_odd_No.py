def Even_Odd(li1):
    even_list = []
    odd_list = []
    for ele in li1:
        if (ele % 2 == 0):
            even_list.append(ele)
        else:
            odd_list.append(ele)
    return even_list, odd_list

n = int(input('How many numbers you want to add in the list :'))
li1 = []
for i in range(n):
    num = int(input(f'Enter the element :'))
    li1.append(num)

Even, Odd = Even_Odd(li1)

print(f'Even numbers list :{Even}')
print(f'Odd numbers list :{Odd}')

