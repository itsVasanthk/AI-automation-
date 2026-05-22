import csv
import os

while True:

    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        task=input("Enter task: ")

        with open(
            "tasks.csv",
            "a",
            newline=""
        ) as file:

            writer=csv.writer(file)

            writer.writerow([task])

        print("Task added.")

    elif choice=="2":

        if not os.path.exists("tasks.csv"):

            print("No tasks found.")

            continue

        with open(
            "tasks.csv",
            "r"
        ) as file:

            reader=csv.reader(file)

            print("\nTasks:\n")

            for index,row in enumerate(reader,start=1):

                print(f"{index}. {row[0]}")

    elif choice=="3":

        tasks=[]

        with open(
            "tasks.csv",
            "r"
        ) as file:

            reader=csv.reader(file)

            tasks=list(reader)

        for index,row in enumerate(tasks,start=1):

            print(f"{index}. {row[0]}")

        delete_index=int(
            input(
                "Enter task number to delete: "
            )
        )

        tasks.pop(delete_index-1)

        with open(
            "tasks.csv",
            "w",
            newline=""
        ) as file:

            writer=csv.writer(file)

            writer.writerows(tasks)

        print("Task deleted.")

    elif choice=="4":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")