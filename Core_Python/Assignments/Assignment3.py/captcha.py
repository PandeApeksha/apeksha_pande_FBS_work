import random

User_ID = input('Enter the User ID :')
password = input('Enter the Password :')

captcha = random.randint(1111, 9999)
print(f'captcha : {captcha}')

captcha_enter = int(input('Enter the captcha :'))

if (captcha == captcha_enter):
    print("Login Success")
else:
    print("Login Failed")
