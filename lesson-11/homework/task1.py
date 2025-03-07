import sqlite3


conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Create the Roster table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# Insert data into the Roster table
characters = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]
cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)

# Update Jadzia Dax to Ezri Dax
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# Query and display Name and Age where Species is Bajoran
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Delete characters older than 100 years
cursor.execute("DELETE FROM Roster WHERE Age > 100")

# Add a new column called Rank
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

# Update Rank values
ranks = {
    "Benjamin Sisko": "Captain",
    "Ezri Dax": "Lieutenant",
    "Kira Nerys": "Major"
}
for name, rank in ranks.items():
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))

# Retrieve all characters sorted by Age in descending order
cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
sorted_characters = cursor.fetchall()
print("Characters sorted by Age:", sorted_characters)


conn.commit()
conn.close()
