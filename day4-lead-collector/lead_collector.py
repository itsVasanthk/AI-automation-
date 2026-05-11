import csv
import os

file_exists = os.path.isfile("leads.csv")

name = input("Enter customer name: ")
email = input("Enter customer email: ")
company = input("Enter company name: ")
phone = input("Enter phone number: ")

with open("leads.csv", "a", newline="") as file:

    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Name", "Email", "Company", "Phone"])

    writer.writerow([name, email, company, phone])

print("Lead saved successfully!")