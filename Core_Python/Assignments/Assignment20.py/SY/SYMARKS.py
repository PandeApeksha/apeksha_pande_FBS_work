class SYMARKS:
    def __init__(self, computer_total, maths_total, electronics_total):
        self.computer_total = computer_total
        self.maths_total = maths_total
        self.electronics_total = electronics_total

    def display(self):
        print(f"Computer Total: {self.computer_total}")
        print(f"Maths Total: {self.maths_total}")
        print(f"Electronics Total: {self.electronics_total}")

    def total_marks(self):
        return self.computer_total + self.maths_total + self.electronics_total

    def average(self):
        return self.total_marks() / 3
