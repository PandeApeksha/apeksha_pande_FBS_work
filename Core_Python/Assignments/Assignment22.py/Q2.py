import pickle
import os

FILENAME = "records.dat"

def add_record():
    """Add a new record to the binary file."""
    record = {}
    record["id"] = input("Enter ID: ")
    record["name"] = input("Enter Name: ")
    record["age"] = input("Enter Age: ")
    record["dept"] = input("Enter Department: ")

    records = []

    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            try:
                records = pickle.load(f)
            except EOFError:
                records = []

    records.append(record)

   
    with open(FILENAME, "wb") as f:
        pickle.dump(records, f)

    print("Record added successfully!\n")


def display_all():
    """Display all records."""
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    with open(FILENAME, "rb") as f:
        try:
            records = pickle.load(f)
            if not records:
                print(" No records found.\n")
                return
            print("\n--- All Records ---")
            for rec in records:
                print(f"ID: {rec['id']}, Name: {rec['name']}, Age: {rec['age']}, Department: {rec['dept']}")
            print()
        except EOFError:
            print("File is empty.\n")


def search_record():
    """Search record by ID."""
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    id_to_search = input("Enter ID to search: ")
    found = False

    with open(FILENAME, "rb") as f:
        try:
            records = pickle.load(f)
            for rec in records:
                if rec["id"] == id_to_search:
                    print(f"\n Record Found: {rec}\n")
                    found = True
                    break
            if not found:
                print("Record not found.\n")
        except EOFError:
            print("File is empty.\n")


def delete_record():
    """Delete record by ID."""
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    id_to_delete = input("Enter ID to delete: ")
    found = False

    with open(FILENAME, "rb") as f:
        try:
            records = pickle.load(f)
        except EOFError:
            records = []

    new_records = [rec for rec in records if rec["id"] != id_to_delete]
    if len(new_records) != len(records):
        found = True

    with open(FILENAME, "wb") as f:
        pickle.dump(new_records, f)

    if found:
        print("Record deleted successfully!\n")
    else:
        print("Record not found.\n")


def edit_record():
    """Edit record by ID."""
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    id_to_edit = input("Enter ID to edit: ")
    found = False

    with open(FILENAME, "rb") as f:
        try:
            records = pickle.load(f)
        except EOFError:
            records = []

    for rec in records:
        if rec["id"] == id_to_edit:
            print("Enter new details (leave blank to keep old value):")
            name = input(f"New Name (old: {rec['name']}): ") or rec["name"]
            age = input(f"New Age (old: {rec['age']}): ") or rec["age"]
            dept = input(f"New Department (old: {rec['dept']}): ") or rec["dept"]
            rec.update({"name": name, "age": age, "dept": dept})
            found = True
            break

    with open(FILENAME, "wb") as f:
        pickle.dump(records, f)

    if found:
        print("Record updated successfully!\n")
    else:
        print("Record not found.\n")


def main():
    """Main menu loop."""
    while True:
        print("===== MENU =====")
        print("1. Add Record")
        print("2. Display All Records")
        print("3. Search Record by ID")
        print("4. Delete Record by ID")
        print("5. Edit Record by ID")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_record()
        elif choice == '2':
            display_all()
        elif choice == '3':
            search_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            edit_record()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
