from empManage import Empmanage

ems = Empmanage()

while True:
    print('\n===== EMPLOYEE MANAGEMENT SYSTEM =====')
    print('1. Add Employee')
    print('2. Update Employee')
    print('3. Delete Employee')
    print('4. Search Employee')
    print('5. Show All Employees')
    print('6. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        ems.addEmp()
    elif choice == '2':
        ems.updEmp()
    elif choice == '3':
        ems.delEmp()
    elif choice == '4':
        ems.searchEmp()
    elif choice == '5':
        ems.showAllEmp()
    elif choice == '6':
        print('Exiting EMS...')
        break
    else:
        print('Invalid choice. Try again.')
