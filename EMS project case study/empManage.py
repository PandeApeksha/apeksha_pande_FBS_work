from emp import Emp

FILE_PATH = r"C:\Users\apeks\OneDrive\Desktop\FBS\Core_Python\EMS project case study\emp_details.txt"


class Empmanage:
    def addEmp(self):
        try:
            id = input('Enter employee ID: ')
            name = input('Enter employee Name: ')
            salary = float(input('Enter salary: '))
            dept = input('Enter department: ')

            emp = Emp(id, name, salary, dept)

            FILE_PATH = 'emp_details.txt'  # saves in same folder
            with open(FILE_PATH, 'a') as fp:
                fp.write(str(emp) + '\n')

            print('Employee added successfully.')

        except Exception as e:
            print('Error:', e)

    def updEmp(self):
        try:
            emp_id = input('Enter employee ID: ')
            allEmpData = []
            found = False

            with open(FILE_PATH, 'r') as fp:
                for line in fp:
                    eList = line.strip().split(', ')

                    if emp_id == eList[0]:
                        found = True

                        if input('Change name (y/n): ').lower() in ['y', 'yes']:
                            eList[1] = input('Enter new name: ')

                        if input('Change salary (y/n): ').lower() in ['y', 'yes']:
                            eList[2] = input('Enter new salary: ')

                        if input('Change department (y/n): ').lower() in ['y', 'yes']:
                            eList[3] = input('Enter new department: ')

                        line = f"{eList[0]}, {eList[1]}, {eList[2]}, {eList[3]}\n"

                    allEmpData.append(line)

            if found:
                with open(FILE_PATH, 'w') as fp:
                    fp.writelines(allEmpData)
                print('Employee updated successfully.')
            else:
                print('Employee not found.')

        except Exception as e:
            print('Error:', e)

    def delEmp(self):
        try:
            emp_id = input('Enter employee ID: ')
            allEmpData = []
            found = False

            with open(FILE_PATH, 'r') as fp:
                for line in fp:
                    eList = line.strip().split(', ')
                    if emp_id == eList[0]:
                        found = True
                    else:
                        allEmpData.append(line)

            if found:
                with open(FILE_PATH, 'w') as fp:
                    fp.writelines(allEmpData)
                print('Employee deleted successfully.')
            else:
                print('Employee not found.')

        except Exception as e:
            print('Error:', e)

    def searchEmp(self):
        try:
            emp_id = input('Enter employee ID: ')
            found = False

            with open(FILE_PATH, 'r') as fp:
                for line in fp:
                    eList = line.strip().split(', ')
                    if emp_id == eList[0]:
                        print('Employee Found:')
                        print(f"ID: {eList[0]}")
                        print(f"Name: {eList[1]}")
                        print(f"Salary: {eList[2]}")
                        print(f"Department: {eList[3]}")
                        found = True
                        break

            if not found:
                print('Employee not found.')

        except Exception as e:
            print('Error:', e)

    def showAllEmp(self):
        try:
            with open(FILE_PATH, 'r') as fp:
                print('\n--- Employee List ---')
                for line in fp:
                    print(line.strip())
        except Exception as e:
            print('Error:', e)
