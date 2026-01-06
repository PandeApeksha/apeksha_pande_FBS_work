import os

for file in ["users.txt", "cars.txt", "bookings.txt"]:
    if not os.path.exists(file):
        open(file, "w").close()


def admin_login():
    u = input("Admin Username: ")
    p = input("Admin Password: ")
    return u == "Apeksha" and p == "Apeksha123"

def car_exists(cid):
    for line in open("cars.txt"):
        if line.startswith(cid + ","):
            return True
    return False

def add_car():
    cid = input("Car ID: ")
    if car_exists(cid):
        print("Car ID already exists!")
        return

    name = input("Car Name: ")
    price = input("Price per day: ")

    with open("cars.txt", "a") as f:
        f.write(f"{cid},{name},{price},Available\n")

    print("Car Added Successfully!")

def view_cars():
    print("\n--- Cars ---")
    for line in open("cars.txt"):
        data = line.strip().split(",")
        if len(data) != 4:
            continue
        cid, name, price, status = data
        print(cid, name, price, status)

def manage_car_status():
    cid = input("Enter Car ID: ")
    cars = []
    updated = False

    for line in open("cars.txt"):
        data = line.strip().split(",")
        if len(data) != 4:
            continue

        if data[0] == cid:
            data[3] = "Available" if data[3] == "Booked" else "Booked"
            updated = True

        cars.append(",".join(data))

    with open("cars.txt", "w") as f:
        f.write("\n".join(cars) + "\n")

    print("Status Updated!" if updated else "Car ID Not Found")

def view_bookings():
    print("\n--- All Bookings ---")
    content = open("bookings.txt").read()
    print(content if content else "No bookings yet.")



def register():
    u = input("Username: ")
    p = input("Password: ")
    open("users.txt", "a").write(f"{u},{p}\n")
    print("Registered Successfully!")

def login():
    u = input("Username: ")
    p = input("Password: ")

    for line in open("users.txt"):
        if line.strip() == f"{u},{p}":
            return u
    return None

def view_available_cars():
    print("\nAvailable Cars:")
    for line in open("cars.txt"):
        data = line.strip().split(",")
        if len(data) != 4:
            continue

        cid, name, price, status = data
        if status == "Available":
            print(cid, name, price)

def book_car(user):
    cid = input("Enter Car ID: ")
    days = input("Number of days: ")

    cars = []
    booked = False

    for line in open("cars.txt"):
        data = line.strip().split(",")
        if len(data) != 4:
            continue

        if data[0] == cid and data[3] == "Available" and not booked:
            data[3] = "Booked"
            open("bookings.txt", "a").write(f"{user},{cid},{days}\n")
            booked = True

        cars.append(",".join(data))

    with open("cars.txt", "w") as f:
        f.write("\n".join(cars) + "\n")

    print("Car Booked!" if booked else "Car not available")

def my_bookings(user):
    print("\nMy Bookings:")
    found = False

    for line in open("bookings.txt"):
        u, cid, days = line.strip().split(",")
        if u == user:
            print(f"Car ID {cid} for {days} days")
            found = True

    if not found:
        print("No bookings found.")


while True:
    print("\n1.Admin\n2.User\n3.Exit")
    ch = input("Select Role: ")

    if ch == "1":
        if admin_login():
            while True:
                print("\n1.Add Car\n2.View Cars\n3.Manage Status\n4.View Bookings\n5.Logout")
                a = input("Choice: ")

                if a == "1":
                    add_car()
                elif a == "2":
                    view_cars()
                elif a == "3":
                    manage_car_status()
                elif a == "4":
                    view_bookings()
                else:
                    break
        else:
            print("Invalid Admin Login!")

    elif ch == "2":
        print("\n1.Register\n2.Login")
        u = input("Choice: ")

        if u == "1":
            register()
        elif u == "2":
            user = login()
            if user:
                while True:
                    print("\n1.View Cars\n2.Book Car\n3.My Bookings\n4.Logout")
                    c = input("Choice: ")

                    if c == "1":
                        view_available_cars()
                    elif c == "2":
                        book_car(user)
                    elif c == "3":
                        my_bookings(user)
                    else:
                        break
            else:
                print("Login Failed!")

    else:
        print("Thank you for using Car Rental System!")
        break
