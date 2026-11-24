
print("STUDENT MANAGEMENT SYSTEM")

name = None
age = None
course = None

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("0. Exit")

    try:
        option = int(input("Choose your option: "))
    except ValueError:
        print("Invalid option. Enter a number.")
        continue

    if option == 1:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            course = input("Enter your course: ")
            print("Student added successfully!")
        except ValueError:
            print("Invalid age. Please enter a number.")
            name = None
            age = None
            course = None

    elif option == 2:
        if name is None:
            print("No student found.")
        else:
            print("Name:", name)
            print("Age:", age)
            print("Course:", course)

    elif option == 3:
        if name is None:
            print("No student found.")
        else:
            search_name = input("Enter name to search: ")

            if search_name.lower() == name.lower():
                print("Name:", name)
                print("Age:", age)
                print("Course:", course)
            else:
                print("Student not found.")

    elif option == 4:
        if name is None:
            print("No student available to update.")
        else:
            update_name = input("Enter name to update: ")

            if update_name.lower() == name.lower():
                name = input("Enter new name: ")

                try:
                    age = int(input("Enter new age: "))
                    course = input("Enter new course: ")
                    print("Student updated successfully!")
                except ValueError:
                    print("Invalid age.")

            else:
                print("Student not found.")

    elif option == 5:
        if name is None:
            print("No student available to delete.")
        else:
            delete_name = input("Enter name to delete: ")

            if delete_name.lower() == name.lower():
                name = None
                age = None
                course = None
                print("Student deleted successfully!")
            else:
                print("Student not found.")

    elif option == 0:
        print("Exiting Student Management System.")
        break

    else:
        print("Invalid option. Choose between 0 and 5.")
