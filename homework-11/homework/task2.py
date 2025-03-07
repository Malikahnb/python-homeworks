import sqlite3


conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create the Books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# Insert data into the Books table
books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
cursor.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", books)

# Update the Year_Published of 1984 to 1950
cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")

#  Query and display Title and Author where Genre is Dystopian
cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
dystopian_books = cursor.fetchall()
print("Dystopian Books:", dystopian_books)

# Delete books published before 1950
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

# Check if the column "Rating" already exists
cursor.execute("PRAGMA table_info(Books)")
columns = [column[1] for column in cursor.fetchall()]

if "Rating" not in columns:
    #  Add a new column called Rating
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")


# Update Rating values
ratings = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}
for title, rating in ratings.items():
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

# Retrieve all books sorted by Year_Published in ascending order
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
sorted_books = cursor.fetchall()
print("Books sorted by Year_Published:", sorted_books)


conn.commit()
conn.close()
