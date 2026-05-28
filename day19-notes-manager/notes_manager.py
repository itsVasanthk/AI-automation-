import csv
import os


def add_note():

    note=input("Enter note: ")

    with open(
        "notes.csv",
        "a",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerow([note])

    print("Note added.")


def view_notes():

    if not os.path.exists("notes.csv"):

        print("No notes found.")

        return

    with open(
        "notes.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        print("\nNotes:\n")

        for index,row in enumerate(
            reader,
            start=1
        ):

            print(
                f"{index}. {row[0]}"
            )


def search_note():

    search=input(
        "Enter keyword: "
    ).lower()

    found=False

    with open(
        "notes.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        for row in reader:

            note=row[0]

            if search in note.lower():

                print(f"\nFound: {note}")

                found=True

    if not found:

        print("No matching note.")


def delete_note():

    with open(
        "notes.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        notes=list(reader)

    for index,row in enumerate(
        notes,
        start=1
    ):

        print(
            f"{index}. {row[0]}"
        )

    delete_index=int(
        input(
            "Enter note number to delete: "
        )
    )

    notes.pop(delete_index-1)

    with open(
        "notes.csv",
        "w",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerows(notes)

    print("Note deleted.")


while True:

    print("\nNotes Manager")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete Note")
    print("5. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        add_note()

    elif choice=="2":

        view_notes()

    elif choice=="3":

        search_note()

    elif choice=="4":

        delete_note()

    elif choice=="5":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")