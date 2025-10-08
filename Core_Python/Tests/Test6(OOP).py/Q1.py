
class Vehicle:
    def __init__(self, persons):
        self.persons = persons

    def calculate_toll(self):
        return 0

class TwoWheeler(Vehicle):
    def calculate_toll(self):
        toll = 20
        if self.persons > 2:
            toll += (self.persons - 2) * 10
        return toll


class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        toll = 30
        if self.persons > 3:
            toll += (self.persons - 3) * 20
        return toll


class FourWheeler(Vehicle):
    def calculate_toll(self):
        toll = 40
        if self.persons > 4:
            toll += (self.persons - 4) * 40
        return toll


class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        toll = 60
        if self.persons > 6:
            toll += (self.persons - 6) * 100
        return toll


while True:
    print("\n--- Toll Calculation System ---")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for using Toll System...")
        break

    persons = int(input("Enter number of persons in vehicle: "))

    if choice == 1:
        v = TwoWheeler(persons)
    elif choice == 2:
        v = ThreeWheeler(persons)
    elif choice == 3:
        v = FourWheeler(persons)
    elif choice == 4:
        v = HeavyVehicle(persons)
    else:
        print("Invalid choice!")
        continue

    print("Total Toll to be paid: Rs", v.calculate_toll())
