import csv
import os


def calculate_grade(mark):

    if mark>=90:

        return "A"

    elif mark>=75:

        return "B"

    elif mark>=50:

        return "C"

    else:

        return "Fail"


def add_student():

    name=input("Enter student name: ")

    try:

        mark=float(
            input("Enter marks: ")
        )

    except ValueError:

        print("Invalid marks.")

        return

    grade=calculate_grade(mark)

    with open(
        "students.csv",
        "a",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerow(
            [name,mark,grade]
        )

    print("Student added.")


def view_students():

    if not os.path.exists(
        "students.csv"
    ):

        print("No student records.")

        return

    with open(
        "students.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        print("\nStudent Records:\n")

        total=0
        count=0

        for row in reader:

            name=row[0]

            mark=float(row[1])

            grade=row[2]

            total+=mark
            count+=1

            print(
                f"{name} | {mark} | {grade}"
            )

        average=total/count

        print(
            f"\nAverage Marks: {average:.2f}"
        )


while True:

    print("\nGrade Manager")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        add_student()

    elif choice=="2":

        view_students()

    elif choice=="3":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")