import requests 
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

with open("users.txt", "w") as file:


    for user in users:
        name = user["name"]
        email = user["email"]
        phone = user["phone"]
        website = user["website"]
        company = user["company"]["name"]

        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")
        file.write(f"Website: {website}\n")
        file.write(f"Company: {company}\n")
        file.write("-" * 30 + "\n")