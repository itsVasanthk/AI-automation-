import csv
import os


def add_contact(name,phone,email):

    with open(
        "contacts.csv",
        "a",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerow(
            [name,phone,email]
        )

    print("Contact added.")


def view_contacts():

    if not os.path.exists(
        "contacts.csv"
    ):

        print("No contacts found.")

        return

    with open(
        "contacts.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        print("\nContacts:\n")

        for row in reader:

            print(
                f"Name: {row[0]}"
            )

            print(
                f"Phone: {row[1]}"
            )

            print(
                f"Email: {row[2]}"
            )

            print("----------------")


def search_contact(keyword):

    found=False

    with open(
        "contacts.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        for row in reader:

            name=row[0]

            if keyword.lower() in name.lower():

                print("\nMatch Found")

                print(
                    f"Name: {row[0]}"
                )

                print(
                    f"Phone: {row[1]}"
                )

                print(
                    f"Email: {row[2]}"
                )

                found=True

    if not found:

        print("Contact not found.")


def delete_contact(index_to_delete):

    with open(
        "contacts.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        contacts=list(reader)

    contacts.pop(index_to_delete-1)

    with open(
        "contacts.csv",
        "w",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerows(contacts)

    print("Contact deleted.")


while True:

    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        name=input("Name: ")
        phone=input("Phone: ")
        email=input("Email: ")

        add_contact(
            name,
            phone,
            email
        )

    elif choice=="2":

        view_contacts()

    elif choice=="3":

        keyword=input(
            "Enter search keyword: "
        )

        search_contact(keyword)

    elif choice=="4":

        view_contacts()

        index=int(
            input(
                "Enter contact number to delete: "
            )
        )

        delete_contact(index)

    elif choice=="5":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")