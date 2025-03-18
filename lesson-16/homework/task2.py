import pandas as pd
import sqlite3

iris_df = pd.read_json("iris.json")

# Rename columns to lowercase
iris_df.columns = iris_df.columns.str.lower()
print("\nRenamed Columns (Iris Dataset):", iris_df.columns)

# Select only sepal_length and sepal_width columns
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print("\nSelected Columns (Iris Dataset):")
print(iris_selected.head())

titanic_df = pd.read_excel("titanic.xlsx")

# 3Filter rows where age > 30
titanic_filtered = titanic_df[titanic_df["Age"] > 30]
print("\nTitanic Passengers Older Than 30:")
print(titanic_filtered.head())

# Count male and female passengers
gender_counts = titanic_df["Sex"].value_counts()
print("\nNumber of Male and Female Passengers:")
print(gender_counts)

flights_df = pd.read_parquet("flights.parquet")

# Extract needed columns
flights_selected = flights_df[['origin', 'dest', 'carrier']]
print("\nSelected Columns (Flights Dataset):")
print(flights_selected.head())

# Find the number of unique destinations
unique_destinations = flights_df['dest'].nunique()
print("\nNumber of Unique Destinations:", unique_destinations)

movie_df = pd.read_csv("movie.csv")

# Filter movies with duration > 120 minutes
long_movies = movie_df[movie_df['duration'] > 120]

# Sort by director_facebook_likes in descending order
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nMovies Longer Than 120 Minutes, Sorted by Director Facebook Likes:")
print(sorted_movies.head())
