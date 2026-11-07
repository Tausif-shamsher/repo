
# Student Performance Analysis System

students = []

def add_student():
    name = input("Enter student name: ")

    marks = []
    subjects = ["Python", "Mathematics", "English"]

    for subject in subjects:
        mark = float(input(f"Enter marks in {subject} (out of 100): "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / len(subjects)

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")


def show_students():
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(f"""
Name: {student['name']}
Total Marks: {student['total']}/300
Percentage: {student['percentage']:.2f}%
Grade: {student['grade']}
""")


def show_topper():
    if not students:
        print("No student records found.")
        return

    topper = max(students, key=lambda x: x["percentage"])

    print("\n--- Top Performing Student ---")
    print("Name:", topper["name"])
    print("Percentage:", topper["percentage"])


def main():
    while True:
        print("\n===== STUDENT PERFORMANCE SYSTEM =====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Show Topper")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            show_topper()
        elif choice == "4":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
