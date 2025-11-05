from SY import SYMARKS
from TY import TYMarks

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_grade(self):
        total_marks = self.sy_marks.computer_total + self.ty_marks.theory
        percentage = (total_marks / 200) * 100  

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return total_marks, percentage, grade

    def display_result(self):
        total, percentage, grade = self.calculate_grade()
        print("\nStudent Result")
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"SY Computer: {self.sy_marks.computer_total}")
        print(f"TY Theory: {self.ty_marks.theory}")
        print(f"Total Marks: {total}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print()

sy = SYMARKS(85, 78, 90)  
ty = TYMarks(88, 92)      

student = Student(101, "Kamini Dukare", sy, ty)
student.display_result()
