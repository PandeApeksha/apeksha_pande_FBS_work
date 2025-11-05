class Student:
    def __init__(self, studentID, name, age, percentage):
        self.studentID = studentID
        self.name = name
        self.age = age
        self.percentage = percentage

    def Display(self):
        print(f"Student ID: {self.studentID}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Percentage: {self.percentage}")

    def __str__(self):
        return f'Student({self.studentID}, {self.name}, {self.age}, {self.percentage})'
    
class College:
    def __init__(self, number_of_students):
        self.NumberOfStudents = number_of_students
        self.students = []

    def AddStudent(self, student):
        if len(self.students) < self.NumberOfStudents:
            self.students.append(student)
            print(f"Student '{student.name}' added successfully.")
        else:
            print("cannot add more students. Limit reached.")

    def GetStudent(self, studentID):
        for s in self.students:
            if s.studentID == studentID:
                return s
        return None
    
    def RemoveStudent(self, studentID):
        for s in self.students:
            if s.studentID == studentID:
                self.students.remove(s)
                print(f"student with ID {studentID} removed successfully.")
                return
        print("student not found.")

    def __str__(self):
        info = f'college with capacity {self.NumberOfStudents}\n'
        info += 'List of Students:\n'
        if not self.students:
            info += 'No students enrolled yet.'
        else:
            for s in self.students:
                info += f" -{s}\n"
        return info
    
College = College(3)

s1 = Student(101, 'Kamini', 21, 85)
s2 = Student(102, 'Neha', 22, 76)
s3 = Student(103, 'Riya', 23, 87)
s4 = Student(104, 'shweta', 24, 68)

College.AddStudent(s1)
College.AddStudent(s2)
College.AddStudent(s3)
College.AddStudent(s4)

print("\ncollege Details:")
print(College)

print("\nsearching for students with ID 102:")
student = College.GetStudent(102)
if student:
    student.Display()
else:
    print('Student not found.')

College.RemoveStudent(101)

print("\ncollege Details After Removal:")
print(College)
