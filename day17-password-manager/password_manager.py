import csv
import os

while True:

    print("\nPassword Manager")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Search Website")
    print("4. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        website=input("Website: ")
        username=input("Username: ")
        password=input("Password: ")

        with open(
            "passwords.csv",
            "a",
            newline=""
        ) as file:

            writer=csv.writer(file)

            writer.writerow(
                [website,username,password]
            )

        print("Password saved.")

    elif choice=="2":

        if not os.path.exists(
            "passwords.csv"
        ):

            print("No passwords saved.")

            continue

        with open(
            "passwords.csv",
            "r"
        ) as file:

            reader=csv.reader(file)

            print("\nSaved Passwords:\n")

            for row in reader:

                print(
                    f"Website: {row[0]}"
                )

                print(
                    f"Username: {row[1]}"
                )

                print(
                    f"Password: {row[2]}"
                )

                print("----------------")

    elif choice=="3":

        search=input(
            "Enter website name: "
        ).lower()

        found=False

        with open(
            "passwords.csv",
            "r"
        ) as file:

            reader=csv.reader(file)

            for row in reader:

                website=row[0]

                if (
                    website.lower()
                    ==
                    search
                ):

                    print("\nMatch Found")

                    print(
                        f"Username: {row[1]}"
                    )

                    print(
                        f"Password: {row[2]}"
                    )

                    found=True

        if not found:

            print("Website not found.")

    elif choice=="4":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")