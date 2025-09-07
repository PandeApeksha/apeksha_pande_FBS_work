m1 = int(input('Enter marks of subject 1:'))
m2 = int(input('Enter marks of subject 2:'))
m3 = int(input('Enter marks of subject 3:'))
m4 = int(input('Enter marks of subject 4:'))
m5 = int(input('Enter marks of subject 5:'))

Gain_Marks = m1 + m2 + m3 + m4 + m5

percentage = (Gain_Marks / 500) * 100

print(f'Percentage is:{percentage}%')