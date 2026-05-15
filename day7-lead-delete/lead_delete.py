import csv

delete_name = input("Enter customer name to delete: ")

updated_rows = []

found = False

with open("leads.csv", "r") as file:

    reader = csv.reader(file)

    header = next(reader)

    updated_rows.append(header)

    for row in reader:

        name = row[0]

        if name.strip().lower() == delete_name.strip().lower():

            print(f"\nDeleting: {row}")

            found = True

            continue

        updated_rows.append(row)

with open("leads.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerows(updated_rows)

if found:
    print("\nLead deleted successfully!")

else:
    print("\nLead not found.")