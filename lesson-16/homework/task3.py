import pandas as pd
import sqlite3

iris_df = pd.read_json("iris.json")

# Calculate mean, median, and standard deviation for each numerical column
iris_stats = iris_df.describe().T[['mean', '50%', 'std']].rename(columns={'50%': 'median'})
print("\nIris Dataset - Mean, Median, and Standard Deviation:")
print(iris_stats)

titanic_df = pd.read_excel("titanic.xlsx")

# Find min, max, and sum of passenger ages
age_min = titanic_df['Age'].min()
age_max = titanic_df['Age'].max()
age_sum = titanic_df['Age'].sum()
print("\nTitanic Passenger Ages:")
print(f"Minimum Age: {age_min}, Maximum Age: {age_max}, Sum of Ages: {age_sum}")

movie_df = pd.read_csv("movie.csv")

# Identify the director with the highest total director_facebook_likes
top_director = movie_df.groupby("director_name")["director_facebook_likes"].sum().idxmax()
print("\nDirector with the Highest Total Facebook Likes:", top_director)

# Find the 5 longest movies and their directors
longest_movies = movie_df.nlargest(5, 'duration')[['title', 'duration', 'director_name']]
print("\nTop 5 Longest Movies and Their Directors:")
print(longest_movies)

flights_df = pd.read_parquet("flights.parquet")

# Check for missing values
missing_values = flights_df.isnull().sum()
print("\nMissing Values in Flights Dataset:")
print(missing_values)

# Fill missing values in a numerical column with its mean
num_col = 'air_time'
if num_col in flights_df.columns:
    flights_df[num_col].fillna(flights_df[num_col].mean(), inplace=True)
    print(f"\nMissing values in '{num_col}' filled with mean.")
