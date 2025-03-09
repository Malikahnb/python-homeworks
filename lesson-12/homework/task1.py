from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extracting weather data
weather_data = []
rows = soup.find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))  # Convert to integer
    condition = cols[2].text
    weather_data.append({"day": day, "temperature": temp, "condition": condition})

# Displaying weather data
print("Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# Finding the highest temperature day
max_temp = max(entry["temperature"] for entry in weather_data)
hottest_days = [entry["day"] for entry in weather_data if entry["temperature"] == max_temp]

print("\nDay(s) with the highest temperature:", ", ".join(hottest_days))

# Finding the days with "Sunny" condition
sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]

print("Sunny day(s):", ", ".join(sunny_days))

# Calculating the average temperature
avg_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"Average temperature for the week: {avg_temp:.2f}°C")
