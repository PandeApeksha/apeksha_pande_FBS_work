class Student:
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
    
class EnggStudent(Student):
    def __init__(self, studentID, name, age, percentage, branch, internal_marks):
        super().__init__(studentID, name, age, percentage)
        self.branch = branch
        self.Internal_marks = internal_marks

    def Accept(self):
        super().Accept()
        self.branch = input("Enter branch :")
        self.Internal_marks = int(input('Enter Internal marks :'))

    def Display(self):
        super().Display
        print(f'Branch :{self.branch}')
        print(f'Internal Marks :{self.Internal_marks}')

    def calculateRank(self):
        total = self.percentage + (self.Internal_marks / 2)
        if total >= 90:
            return "Excellent"
        elif total >= 75:
            return "Very Good"
        elif total >= 60:
            return "Good"
        elif total >= 50:
            return "Average"
        else:
            return "Poor"

    def __str__(self):
        return(f'EnggStudent({self.studentID}, {self.name}, {self.age}, '
               f'{self.percentage}, Branch:{self.branch}, Internal_marks:{self.Internal_marks})') 

print("\nUsing Parameterized Constructor:")
e1 = EnggStudent(201, "Kamini", 21, 86, "Computer", 45)
e1.Display()

# Using Accept() method
print("\nEnter details for another engineering student:")
e2 = EnggStudent(0, "", 0, 0.0, "", 0.0)
e2.Accept()

print("\nUsing Accept() Method:")
e2.Display()

# Demonstrate __str__ method
print("\nUsing __str__ Method:")
print(e1)   
