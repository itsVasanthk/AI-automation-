import csv

search_name = input("Enter customer name to update: ")

updated_rows = []

found = False

with open("leads.csv", "r") as file:

    reader = csv.reader(file)

    header = next(reader)

    updated_rows.append(header)

    for row in reader:

        name = row[0]

        print(name)

        if name.strip().lower() == search_name.strip().lower():

            print(f"\nFound lead: {row}")

            new_company = input("Enter new comapny: ")
            new_phone = input("Enter new phone: ")

            row[2] = new_company
            row[3] = new_phone

            found = True

        updated_rows.append(row)

with open("leads.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(updated_rows)

if found:
    print("\nLead updated successfully!")

else:
    print("\nLead not found")