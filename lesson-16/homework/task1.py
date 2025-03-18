import sqlite3
import pandas as pd

# Reading SQLite Database
db_connection = sqlite3.connect("chinook.db")
cursor = db_connection.cursor()

customers_df = pd.read_sql_query("SELECT * FROM customers", db_connection)
print("Customers Table (First 10 Rows):")
print(customers_df.head(10))

db_connection.close()

# Reading JSON File
iris_df = pd.read_json("iris.json")
print("\nIris Dataset Shape:", iris_df.shape)
print("Column Names:", iris_df.columns.tolist())

# Reading Excel File
titanic_df = pd.read_excel("titanic.xlsx")
print("\nTitanic Dataset (First 5 Rows):")
print(titanic_df.head())

# Reading Parquet File
flights_df = pd.read_parquet("flights.parquet")
print("\nFlights Dataset Info:")
print(flights_df.info())

# Reading CSV File
movies_df = pd.read_csv("movie.csv")
print("\nMovie Dataset (Random Sample of 10 Rows):")
print(movies_df.sample(10))
