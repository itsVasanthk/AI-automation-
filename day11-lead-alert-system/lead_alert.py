import csv
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

name = input("Name: ")
email = input("Email: ")
company = input("Company: ")
phone = input("Phone: ")

with open("leads.csv", "a",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        [name,email,company,phone]
    )

subject = "New Lead Added"

message=f"""
New Lead Received

Name: {name}
Email: {email}
Company: {company}
Phone: {phone}
"""

text=f"Subject:{subject}\n\n{message}"

server=smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    email_address,
    email_password
)

server.sendmail(
    email_address,
    email_address,
    text
)

server.quit()

print("Lead saved + email sent")