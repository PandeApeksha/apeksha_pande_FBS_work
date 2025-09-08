user = "Kamini"
Pass = "KD123"
attempts = 3

for i in range(1, attempts + 1):
    userID = input('Enter the userID :')
    Password = input('Enter the Password :')

    if (user == userID):
        print('Login Successfully.')
        break
    else:
        if (i < attempts):
            print('Invalid Credentials.')
        else:
            print('Program Terminated.')
