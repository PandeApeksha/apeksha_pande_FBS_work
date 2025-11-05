class TYMarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def display(self):
        print(f"Theory Marks: {self.theory}")
        print(f"Practical Marks: {self.practical}")

    def total(self):
        return self.theory + self.practical

    def average(self):
        return self.total() / 2
