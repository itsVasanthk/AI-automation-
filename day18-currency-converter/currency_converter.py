import requests

print("\nCurrency Converter\n")

base=input(
    "Enter base currency (USD/INR/EUR): "
).upper()

target=input(
    "Enter target currency: "
).upper()

amount=float(
    input("Enter amount: ")
)

url=f"https://api.exchangerate-api.com/v4/latest/{base}"

response=requests.get(url)

data=response.json()

rates=data["rates"]

if target in rates:

    rate=rates[target]

    converted=amount*rate

    print(
        f"\n{amount} {base} = {converted:.2f} {target}"
    )

else:

    print("Invalid target currency.")