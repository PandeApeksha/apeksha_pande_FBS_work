for i in range(1,6):
    for j in range(i,6):
        if(i == 1 or j == i or i+j == 5 + i):
             print(j, end = ' ')
        else:
            print(' ', end = ' ')
        
    print()
