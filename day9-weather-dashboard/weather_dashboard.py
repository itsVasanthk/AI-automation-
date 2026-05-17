import requests

cities = {
    "chennai": (13.08, 80.27),
    "banglore": (12.97, 77.59),
    "hyderabad": (17.38, 78.48),
    "mumbai": (19.07, 72.87),
    "madurai": (9.92, 78.11)
}

city = input("Enter city: ").lower()

if city in cities:

    latitude, longitude = cities[city]

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    response = requests.get(url)

    data = response.json()

    weather = data["current_weather"]

    temperature = weather["temperature"]
    windspeed = weather["windspeed"]

    print("\nWeather Report")
    print("-----------------------")
    print(f"City: {city.title()}")
    print(f"Temperature: {temperature}°C")
    print(f"Wind Speed: {windspeed} km/h")

else:
    print("City not available.")