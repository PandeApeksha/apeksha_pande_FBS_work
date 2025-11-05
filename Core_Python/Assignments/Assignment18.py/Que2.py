class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        print(f"Constructor called: Distance({self.km} km, {self.m} m, {self.cm} cm) created")

    def __del__(self):
        print(f"Destructor called: Distance({self.km} km, {self.m} m, {self.cm} cm) destroyed")

    def normalize(self):
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km += self.m // 1000
        self.m = self.m % 1000

    def __add__(self, other):
        temp_km = self.km + other.km
        temp_m = self.m + other.m
        temp_cm = self.cm + other.cm

        result = Distance(temp_km, temp_m, temp_cm)
        result.normalize()
        return result

    def __sub__(self, other):
        total_cm1 = (self.km * 100000) + (self.m * 100) + self.cm
        total_cm2 = (other.km * 100000) + (other.m * 100) + other.cm

        diff_cm = abs(total_cm1 - total_cm2)

        km = diff_cm // 100000
        diff_cm = diff_cm % 100000
        m = diff_cm // 100
        cm = diff_cm % 100

        return Distance(km, m, cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"

d1 = Distance(2, 850, 75)
d2 = Distance(1, 900, 50)

print("\nFirst Distance:", d1)
print("Second Distance:", d2)

d3 = d1 + d2
print("\nAfter Addition:")
print("Result =", d3)

d4 = d1 - d2
print("\nAfter Subtraction:")
print("Result =", d4)
