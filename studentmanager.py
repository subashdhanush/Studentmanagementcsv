import csv
import os

FILENAME = "students.csv"

# Check if file exists, if not create with headers
if not os.path.isfile(FILENAME):
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Age", "Course"])

# Add a new student
def add_student():
    roll = input("Enter Roll Number: ")
    if student_exists(roll):
        print("Student with this Roll Number already exists!\n")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, age, course])
    print("Student added successfully!\n")

# View all students
def view_students():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        students = list(reader)

        if len(students) <= 1:
            print("No student records found.\n")
            return

        print("\n--- Student Records ---")
        for row in students:
            print("\t".join(row))
        print()

# Search student by Roll No
def search_student():
    roll = input("Enter Roll Number to search: ")
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("Student Found:")
                print("Roll No:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Course:", row[3])
                return
        print("Student not found.\n")

# Update student
def update_student():
    roll = input("Enter Roll Number to update: ")
    updated = False
    students = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                print("Current Data: ", row)
                name = input("Enter New Name: ")
                age = input("Enter New Age: ")
                course = input("Enter New Course: ")
                students.append([roll, name, age, course])
                updated = True
            else:
                students.append(row)

    if updated:
        with open(FILENAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print("Student updated successfully!\n")
    else:
        print("Student not found.\n")

# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    deleted = False
    students = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                deleted = True
                continue
            students.append(row)

    if deleted:
        with open(FILENAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(students)
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")

# Helper: Check if student exists
def student_exists(roll):
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == roll:
                return True
    return False

# Main Menu
def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()
