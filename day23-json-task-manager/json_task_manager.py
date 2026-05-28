import json
import os


def load_tasks():

    if not os.path.exists(
        "tasks.json"
    ):

        return []

    with open(
        "tasks.json",
        "r"
    ) as file:

        return json.load(file)


def save_tasks(tasks):

    with open(
        "tasks.json",
        "w"
    ) as file:

        json.dump(
            tasks,
            file,
            indent=4
        )


def add_task():

    tasks=load_tasks()

    task=input("Enter task: ")

    tasks.append(task)

    save_tasks(tasks)

    print("Task added.")


def view_tasks():

    tasks=load_tasks()

    if not tasks:

        print("No tasks found.")

        return

    print("\nTasks:\n")

    for index,task in enumerate(
        tasks,
        start=1
    ):

        print(f"{index}. {task}")


def delete_task():

    tasks=load_tasks()

    view_tasks()

    delete_index=int(
        input(
            "Enter task number to delete: "
        )
    )

    tasks.pop(delete_index-1)

    save_tasks(tasks)

    print("Task deleted.")


while True:

    print("\nJSON Task Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        add_task()

    elif choice=="2":

        view_tasks()

    elif choice=="3":

        delete_task()

    elif choice=="4":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")