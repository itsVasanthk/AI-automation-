import requests

cities = {
    "chennai": (13.08,80.27),
    "bangalore": (12.97,77.59),
    "hyderabad": (17.38,78.48),
    "mumbai": (19.07,72.87),
    "delhi": (28.61,77.20)
}

with open("weather_report.txt","w", encoding="utf-8") as report:
    report.write("Weather Summary\n\n")

    for city,(lat,long) in cities.items():

        url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current_weather=true"

        response=requests.get(url)

        data=response.json()

        weather=data["current_weather"]

        temp=weather["temperature"]

        wind=weather["windspeed"]

        output=f"{city.title()} → {temp}°C | Wind:{wind}\n"

        print(output)

        report.write(output)

print("\nReport generated successfully.")