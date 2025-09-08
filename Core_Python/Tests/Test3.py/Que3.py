n = int(input('Enter the no. of employee :'))
total_Emp = 0

for i in range(1, n + 1):
    salary = int(input(f'Enter the basic salary of employee {i} :'))

    if (salary < 20000):
        da = (salary / 100) * 10
        ta = (salary / 100) * 12
        hra = (salary / 100) * 15
    else:
        da = (salary / 100) * 15
        ta = (salary / 100) * 18
        hra = (salary / 100) * 20

    total_salary = salary + da + ta + hra
    print(f'total salary of employee {i}: {total_salary}')
    total_Emp += total_salary

print(f'total salary of all employee is : {n * total_salary}')
