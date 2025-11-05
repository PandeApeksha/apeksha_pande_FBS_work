class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
        print(f"Constructor called: ComplexNumber({self.real}, {self.imag}) created")

    def __del__(self):
        print(f"Destructor called: ComplexNumber({self.real}, {self.imag}) destroyed")

    def __add__(self, other):
        result_real = self.real + other.real
        result_imag = self.imag + other.imag
        return ComplexNumber(result_real, result_imag)

    def __sub__(self, other):
        result_real = self.real - other.real
        result_imag = self.imag - other.imag
        return ComplexNumber(result_real, result_imag)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, -4)

print("\nFirst Complex Number:", c1)
print("Second Complex Number:", c2)

c3 = c1 + c2
print("\nAfter Addition:")
print("Result =", c3)

c4 = c1 - c2
print("\nAfter Subtraction:")
print("Result =", c4)
