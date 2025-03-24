import requests

API_KEY = "1607d96446ed9b7d915ff0669d336091"
CITY = input("Enter city: ")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch weather data
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    # Extract weather details
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_description = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather_description.capitalize()}")
else:
    print("Failed to fetch weather data. Check your API key and city name.")