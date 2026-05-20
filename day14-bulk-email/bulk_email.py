import csv
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    email_address,
    email_password
)

with open("leads.csv","r") as file:

    reader=csv.reader(file)

    next(reader)

    for row in reader:

        name=row[0]
        email=row[1]

        subject="Hello"

        message=f"""
Hi {name},

This email was sent using Python automation.

-Vasanth
"""

        text=f"Subject:{subject}\n\n{message}"

        server.sendmail(
            email_address,
            email,
            text
        )

        print(
            f"Sent to {email}"
        )

server.quit()

print("\nAll emails sent.")