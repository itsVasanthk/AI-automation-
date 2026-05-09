import requests
url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&current_weather=true"
response = requests.get(url)
data = response.json()
temperature = data["current_weather"]["temperature"]
windspeed = data["current_weather"]["windspeed"]
time = data["current_weather"]["time"]
print(f"Current temperature is {temperature}°C")
print(f"Windspeed is {windspeed} km/h")
print(f"Time: {time}")