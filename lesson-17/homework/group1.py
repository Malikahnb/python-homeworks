import pandas as pd

# Titanic Dataset Analysis

titanic_df = pd.read_csv("titanic.csv")

# Group by Pclass and calculate average age, total fare, and passenger count
titanic_grouped = titanic_df.groupby("Pclass").agg(
    avg_age=("Age", "mean"),
    total_fare=("Fare", "sum"),
    passenger_count=("PassengerId", "count")
)

print("\nTitanic Grouped Data:")
print(titanic_grouped)


# Movie Dataset Analysis
movies_df = pd.read_csv("movie.csv")

# Group by color and director_name
movie_grouped = movies_df.groupby(["color", "director_name"]).agg(
    total_reviews=("num_critic_for_reviews", "sum"),
    avg_duration=("duration", "mean")
)

print("\nMovies Grouped Data:")
print(movie_grouped)


# Flights Dataset Analysis
flights_df = pd.read_csv("flights.csv")

# Group by Year and Month
flights_grouped = flights_df.groupby(["Year", "Month"]).agg(
    total_flights=("FlightNum", "count"),
    avg_arrival_delay=("ArrDelay", "mean"),
    max_departure_delay=("DepDelay", "max")
)

print("\nFlights Grouped Data:")
print(flights_grouped)
