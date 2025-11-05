class Student:
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Student Name: ")
        self.Age = int(input("Enter Student Age: "))
        self.Percentage = float(input("Enter Student Percentage: "))

    def Display(self):
        print(f"Student ID: {self.StudentId}")
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Percentage: {self.Percentage}%")
        print(f"Rank: {self.CalculateRank()}")

    def CalculateRank(self):
        if self.Percentage >= 85:
            return "A+"
        elif self.Percentage >= 70:
            return "A"
        elif self.Percentage >= 60:
            return "B"
        elif self.Percentage >= 50:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"Student({self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}%)"

class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_internship):
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_internship

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Internship Marks: "))

    def Display(self):
        super().Display()
        print(f"Specialization: {self.Specialization}")
        print(f"Internship Marks: {self.MarksOfInternship}")
        print(f"Final Rank: {self.CalculateRank()}")

    def CalculateRank(self):
        total_score = (self.Percentage * 0.7) + (self.MarksOfInternship * 0.3)
        if total_score >= 90:
            return "Outstanding"
        elif total_score >= 75:
            return "Excellent"
        elif total_score >= 60:
            return "Good"
        elif total_score >= 50:
            return "Average"
        else:
            return "Needs Improvement"

    def __str__(self):
        return (f"MedicalStudent({self.StudentId}, {self.Name}, {self.Age}, "
                f"{self.Percentage}%, Specialization: {self.Specialization}, "
                f"Internship Marks: {self.MarksOfInternship})")

print("\nUsing Parameterized Constructor:")
m1 = MedicalStudent(301, "Kamini", 22, 87, "Cardiology", 92)
m1.Display()

print("\nEnter details for another Medical Student:")
m2 = MedicalStudent(0, "", 0, 0.0, "", 0.0)
m2.Accept()

print("\nUsing Accept() Method:")
m2.Display()

print("\nUsing __str__ Method:")
print(m1)
