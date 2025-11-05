class student:
    def __init__(self, studentID, name, age, percentage):
        self.studentID = studentID
        self.name = name
        self.age = age
        self.percentage = percentage

    def Accept(self):
        self.studentID = int(input('Enter Student ID :'))
        self.name = input("Enter student Name :")
        self.age = int(input("Enter student Age :"))
        self.percentage = int(input("Enter percentage :"))

    def Display(self):
        print(f'student ID :{self.studentID}')
        print(f'Name :{self.name}')
        print(f'Age :{self.age}')
        print(f'percentage :{self.percentage}')
        print(f'Rank :{self.calculateRank()}')

    def calculateRank(self):
        if self.percentage >= 85:
            return "A+"
        elif self.percentage >= 70:
            return "A"
        elif self.percentage >= 60:
            return "B"
        elif self.percentage >= 50:
            return "C"
        else:
            return "Fail"
        
    def __str__(self):
        return f'student({self.studentID}, {self.name}, {self.age}, {self.percentage})'
    
s1 = student(101, "Kamini", 21, 81)
print("\nUsing Parameterized Constructor:")
s1.Display()

# Using Accept() method
print("\nEnter details for another student:")
s2 = student(0, "", 0, 0)
s2.Accept()
print("\nUsing Accept() Method:")
s2.Display()

# Demonstrating __str__ method
print("\nUsing __str__ Method:")
print(s1)