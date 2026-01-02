import os


if not os.path.exists("users.txt"): open("users.txt","w").close()
if not os.path.exists("cars.txt"): open("cars.txt","w").close()
if not os.path.exists("bookings.txt"): open("bookings.txt","w").close()

def admin_login():
    u = input("Admin Username: ")
    p = input("Admin Password: ")
    return u=="Apeksha" and p=="Apeksha123"

def add_car():
    cid = input("Car ID: ")
    name = input("Car Name: ")
    price = input("Price per day: ")
    with open("cars.txt","a") as f:
        f.write(f"{cid},{name},{price},Available\n")
    print("Car Added!")

def view_cars():
    print("\n--- Cars ---")
    with open("cars.txt","r") as f:
        for line in f:
            cid,name,price,status = line.strip().split(",")
            print(cid,name,price,status)

def manage_car_status():
    cid = input("Enter Car ID to change status: ")
    cars = []
    with open("cars.txt","r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0]==cid:
                data[3]="Available" if data[3]=="Booked" else "Booked"
            cars.append(",".join(data))
    open("cars.txt","w").write("\n".join(cars))
    print("Status Updated!")

def view_bookings():
    print("\n--- Bookings ---")
    print(open("bookings.txt").read())


def register():
    u = input("Username: ")
    p = input("Password: ")
    open("users.txt","a").write(f"{u},{p}\n")
    print("Registered Successfully!")

def login():
    u = input("Username: ")
    p = input("Password: ")
    for line in open("users.txt"):
        if line.strip()==f"{u},{p}":
            return u
    return None

def view_available_cars():
    print("\nAvailable Cars:")
    for line in open("cars.txt"):
        cid,name,price,status = line.strip().split(",")
        if status=="Available":
            print(cid,name,price)

def book_car(user):
    cid = input("Enter Car ID: ")
    days = input("Number of days: ")
    cars=[]
    booked=False
    for line in open("cars.txt"):
        data=line.strip().split(",")
        if data[0]==cid and data[3]=="Available":
            data[3]="Booked"
            open("bookings.txt","a").write(f"{user},{cid},{days}\n")
            booked=True
        cars.append(",".join(data))
    open("cars.txt","w").write("\n".join(cars))
    print("Car Booked!" if booked else "Car not available")

def my_bookings(user):
    print("\nMy Bookings:")
    for line in open("bookings.txt"):
        u,cid,days=line.strip().split(",")
        if u==user:
            print(cid,"for",days,"days")


while True:
    print("\n1.Admin\n2.User\n3.Exit")
    ch=input("Select Role: ")

    if ch=="1":
        if admin_login():
            while True:
                print("\n1.Add Car\n2.View Cars\n3.Manage Status\n4.View Bookings\n5.Logout")
                a=input("Choice: ")
                if a=="1": add_car()
                elif a=="2": view_cars()
                elif a=="3": manage_car_status()
                elif a=="4": view_bookings()
                else: break
        else:
            print("Invalid Admin Login!")

    elif ch=="2":
        print("\n1.Register\n2.Login")
        u=input("Choice: ")
        if u=="1": register()
        elif u=="2":
            user=login()
            if user:
                while True:
                    print("\n1.View Cars\n2.Book Car\n3.My Bookings\n4.Logout")
                    c=input("Choice: ")
                    if c=="1": view_available_cars()
                    elif c=="2": book_car(user)
                    elif c=="3": my_bookings(user)
                    else: break
            else:
                print("Login Failed!")

    else:

        break
