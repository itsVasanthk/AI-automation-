import csv

companies = {}

total_leads = 0

with open("leads.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        
        total_leads += 1

        company = row[2]

        if company in companies:

            companies[company] += 1
        else:

            companies[company] = 1

print(f"\nTotal Leads: {total_leads}")

print("\nCompanies: \n")

for company, count in companies.items():

    print(f"{company}: {count}")
