
import pickle
class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print(f"Employee ID: {self.eid}")
        print(f"Employee Name: {self.ename}")
        print(f"Basic Salary: {self.basic}")
emp1 = Emp(101, "Apeksha", 50000)


with open("emp_data.pkl", "wb") as f:
    pickle.dump(emp1, f)
print("Employee object has been pickled (saved to file).")


with open("emp_data.pkl", "rb") as f:
    emp_loaded = pickle.load(f)
print("Employee object has been unpickled (loaded from file).")

print("\nUnpickled Employee Data:")
emp_loaded.display()
