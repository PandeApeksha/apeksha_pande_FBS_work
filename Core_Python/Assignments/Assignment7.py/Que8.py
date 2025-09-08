k = 7
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = ' ')

    for k in range(1,k+1):
        print(' ', end = ' ')
    k -= 2

    for j in range(i-1, 0, -1):
        if(i==5 and j == 1):
            print('', end = '')
        else:
            print(j, end = ' ')
    print()