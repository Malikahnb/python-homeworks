import pandas as pd

# TITANIC
titanic_df = pd.read_csv("titanic.csv")

# Function to classify age
def classify_age(age):
    return "Child" if age < 18 else "Adult"

# Apply function to create Age_Group column
titanic_df["Age_Group"] = titanic_df["Age"].apply(classify_age)

# Display results
print("Titanic Data:")
print(titanic_df.head())


# EMPLOYEE
employee_df = pd.read_csv("employee.csv")

# Normalize salaries within each department
employee_df["Normalized_Salary"] = employee_df.groupby("Department")["Salary"].transform(
    lambda x: (x - x.min()) / (x.max() - x.min())
)

# Display results
print("\nEmployee Data:")
print(employee_df)


# MOVIE
movies_df = pd.read_csv("movie.csv")

# Function to classify movie length
def classify_duration(duration):
    if duration < 60:
        return "Short"
    elif 60 <= duration <= 120:
        return "Medium"
    else:
        return "Long"

# Apply function to create Movie_Length column
movies_df["Movie_Length"] = movies_df["duration"].apply(classify_duration)

print("\nMovie Data:")
print(movies_df.head())
