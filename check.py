students = []

def add_student():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    courses = [c.strip() for c in input("Enter courses (comma separated): ").split(",")]

    students.append({
        "id": id,
        "name": name,
        "age": age,
        "courses": courses
    })

    print("\nStudent added successfully!\n")

    # Show updated list immediately
    print("Updated Student List:")
    view_students()


def view_students():
    if not students:
        print("No students\n")
        return

    for s in students:
        print("ID:", s["id"])
        print("Name:", s["name"])
        print("Age:", s["age"])
        print("Courses:", ", ".join(s["courses"]))
        print()


def search_student():
    id = input("Enter ID: ")

    for s in students:
        if s["id"] == id:
            print("\nStudent Found:")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Courses:", ", ".join(s["courses"]))
            print()
            return

    print("Not found\n")


def get_unique_courses():
    c_set = set()

    for s in students:
        for c in s["courses"]:
            c_set.add(c)

    print("Unique Courses:", c_set, "\n")


def remove_student():
    id = input("Enter ID: ")

    for i in range(len(students)):
        if students[i]["id"] == id:
            del students[i]
            print("Removed successfully!\n")
            return

    print("Not found\n")


def menu_switch(choice):
    return {
        "1": add_student,
        "2": view_students,
        "3": search_student,
        "4": get_unique_courses,
        "5": remove_student
    }.get(choice)


while True:
    print("===== MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Show Unique Courses")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "6":
        print("Exiting program...")
        break

    action = menu_switch(choice)

    if action:
        action()
    else:
        print("Invalid choice\n")