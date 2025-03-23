import pandas as pd

# Load Titanic dataset
titanic_df = pd.read_csv("titanic.csv")


# Define pipeline functions
def filter_survived(df):
    return df[df["Survived"] == 1]


def fill_missing_age(df):
    df["Age"].fillna(df["Age"].mean(), inplace=True)
    return df


def add_fare_per_age(df):
    df["Fare_Per_Age"] = df["Fare"] / df["Age"]
    return df


# Apply pipeline using pipe()
titanic_processed = (titanic_df
                     .pipe(filter_survived)
                     .pipe(fill_missing_age)
                     .pipe(add_fare_per_age))

print(titanic_processed.head())


flights_df = pd.read_csv("flights.csv")


# Define pipeline functions
def filter_delayed_flights(df):
    return df[df["DepDelay"] > 30]


def add_delay_per_hour(df):
    df["Delay_Per_Hour"] = df["DepDelay"] / df["ScheduledTime"]
    return df


# Apply pipeline using pipe()
flights_processed = (flights_df
                     .pipe(filter_delayed_flights)
                     .pipe(add_delay_per_hour))

# Display result
print("\n\nFlights Data:")
print(flights_processed.head())
