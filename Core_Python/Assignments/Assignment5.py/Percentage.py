students = int(input('Enter Number of Students :'))
total_perc = 0

for i in range(1, students + 1):
    print(f'Enter marks of student {i} :')
    gain_marks = 0
    for j in range(1,6):
        marks = int(input(f'Enter marks of subjects {j} :'))
        gain_marks = gain_marks + marks
    percentage = gain_marks / 500 * 100
    total_perc = total_perc + percentage
    print(f'Percentage of student {i} : {percentage}%')

Average = total_perc / students
print(f'Average percentage is : {Average}%')
