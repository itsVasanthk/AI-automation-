import csv
import os


def add_expense():

    category=input(
        "Enter category: "
    )

    amount=float(
        input("Enter amount: ")
    )

    with open(
        "expenses.csv",
        "a",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerow(
            [category,amount]
        )

    print("Expense added.")


def view_expenses():

    if not os.path.exists(
        "expenses.csv"
    ):

        print("No expenses found.")

        return

    total=0

    with open(
        "expenses.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        print("\nExpenses:\n")

        for row in reader:

            category=row[0]

            amount=float(row[1])

            total+=amount

            print(
                f"{category}: ₹{amount}"
            )

    print(
        f"\nTotal Spending: ₹{total}"
    )


def category_analysis():

    categories={}

    with open(
        "expenses.csv",
        "r"
    ) as file:

        reader=csv.reader(file)

        for row in reader:

            category=row[0]

            amount=float(row[1])

            if category in categories:

                categories[category]+=amount

            else:

                categories[category]=amount

    print("\nCategory Analysis:\n")

    for category,total in categories.items():

        print(
            f"{category}: ₹{total}"
        )


while True:

    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Analysis")
    print("4. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        add_expense()

    elif choice=="2":

        view_expenses()

    elif choice=="3":

        category_analysis()

    elif choice=="4":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")