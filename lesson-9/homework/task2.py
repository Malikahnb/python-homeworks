import csv
from collections import defaultdict

# Step 1: Read data from grades.csv
grades_file = "grades.csv"

grades_data = []
with open(grades_file, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  # Convert grade to integer
        grades_data.append(row)

# Step 2: Calculate average grade per subject
subject_grades = defaultdict(list)

for entry in grades_data:
    subject_grades[entry["Subject"]].append(entry["Grade"])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

# Step 3: Write results to average_grades.csv
output_file = "average_grades.csv"

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])  # Header row
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, round(avg_grade, 2)])  # Round to 2 decimal places

print("Average grades have been written to average_grades.csv successfully.")
