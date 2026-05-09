import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

receiver_email = "vasanthkraja77@gmail.com"

subject = "python automation test"

message = """
Hello,

 this email was sent automatically using python.

 - vasanth
 """

email_text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(email_address, email_password)

server.sendmail(email_address, receiver_email, email_text)

print("Email sent successfully!")

server.quit()