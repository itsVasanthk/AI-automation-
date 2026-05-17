import requests
import urllib3
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.quotable.io/random"

response = requests.get(url, verify=False)

data = response.json()

quote = data["content"]
author = data["author"]

current_time = datetime.now()

print(f"\nQuote:")
print(f"{quote}")

print(f"\nAuthor: {author}")

with open("quote_history.txt", "a") as file:

    file.write(
        f"{current_time} | {quote} - {author}\n"
    )

print("\nSaved to history.")