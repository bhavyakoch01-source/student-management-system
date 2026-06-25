students = []
def add_student():
    Name = input("Enter Your Name : ")
    Roll = input("Enter Roll Number : ")
    Class = input("Enter Class : ")
    Marks = input("Enter Marks : ")

    student = {
        "Name" : Name,
        "Roll" : Roll,
        "Class" : Class,
        "Marks" : Marks
    }

    students.append(student)
    print("Student Added Sucessfully!\n")

def view_students():
    if len(students) == 0:
        print("No student Recorded")

    else:
        print("\n--- Student Record ---")
        for student in students:
            print(f"Name: {student['Name']}")
            print(f"Roll No: {student['Roll']}")
            print(f"Class: {student['Class']}")
            print(f"Marks: {student['Marks']}")
            print("-------------------------------")
        print()

def search_student():
    Roll = input("Enter Roll NUmber To Search : ")
    for student in students:
        if student["Roll"] == Roll:
            print("\n student Found!")
            print(f"Name: {student['Name']}")
            print(f"Class: {student['Class']}")
            print(f"Marks: {student['Marks']}\n")
            return
        print("student Not Found. \n")


def delete_student():
    Roll = input("Enter Roll Number To Delete : ")

    for student in students:
        if student["Roll"] == Roll:
            students.remove(student)
            print("student Deleted Sucessfully! \n")

            return
            print("student Not Found : ")


while True:
    print("============Student Management System============")
    print("1. Add Student")
    print("2. view student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank You For Using Student Management System!")
        break

    else:
        print("Invalid Choice. Try Again. \n")