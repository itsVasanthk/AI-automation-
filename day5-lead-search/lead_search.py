import csv

search = input("Enter customer name or email to search: ")

with open("leads.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    found = False

    for row in reader:

        name = row[0]
        email = row[1]
        company = row[2]
        phone = row[3]

        if search.lower() == name.lower() or search.lower() == email.lower():

            print("\nLead Found:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Company: {company}")
            print(f"Phone: {phone}")

            found = True

    if not found:
        print("Lead not found.")