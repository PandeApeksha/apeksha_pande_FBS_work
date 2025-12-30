from empManage import Empmanage

class Admin:
    def __init__(self):
        em1 = Empmanage()
        ch = 0
        while(ch != '7'):
            print('''Please select option
            1. Add employee
            2. Update employee
            3. Delete employee
            4. Search employee
            5. Show all employees
            6. Change password
            7. Exit''')
            ch = input('Enter choice:')
            if(ch == '1'):
                em1.addEmp()
            elif(ch == '2'):
                em1.updEmp()
            elif(ch == '3'):
                em1.delEmp()
            elif(ch == '4'):
                em1.searchEmp()
            elif(ch == '5'):
                em1.showAllEmp()
            elif(ch == '6'):
                Admin.changePassword()
            elif(ch == '7'):
                print('Logged out...')
            else:
                print('Invalid choice...')
    # @staticmethod
    def changePassword():
        print("Changing password")

if(__name__ == '__main__'):
    a = Admin()