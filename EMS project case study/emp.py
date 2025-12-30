class Emp:
    def __init__(self, id, name, salary, dept):
        self.id = id
        self.name = name
        self.salary = salary
        self.dept = dept

    def __str__(self):
        return f"{self.id}, {self.name}, {self.salary}, {self.dept}"
