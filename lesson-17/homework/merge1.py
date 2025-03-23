import sqlite3
import pandas as pd

# Load the Chinook database
db_connection = sqlite3.connect("chinook.db")

cursor = db_connection.cursor()

# Perform INNER JOIN between customers and invoices on CustomerId
query = """
SELECT customer.CustomerId, customer.FirstName, customer.LastName, COUNT(invoice.InvoiceId) AS TotalInvoices
FROM customer
INNER JOIN invoice ON customer.CustomerId = invoice.CustomerId
GROUP BY customer.CustomerId
ORDER BY TotalInvoices DESC;
"""

customers_invoices_df = pd.read_sql_query(query, db_connection)
print("Total Number of Invoices for Each Customer:")
print(customers_invoices_df)

db_connection.close()

# Load movie dataset
movies_df = pd.read_csv("movie.csv")

# Create two DataFrames
df1 = movies_df[['director_name', 'color']].drop_duplicates()
df2 = movies_df[['director_name', 'num_critic_for_reviews']].drop_duplicates()

# Perform LEFT JOIN on director_name
left_join_df = pd.merge(df1, df2, on="director_name", how="left")

# Perform FULL OUTER JOIN (using outer join)
full_outer_join_df = pd.merge(df1, df2, on="director_name", how="outer")

# Print the number of rows in each join type
print("\nNumber of rows after LEFT JOIN:", len(left_join_df))
print("Number of rows after FULL OUTER JOIN:", len(full_outer_join_df))
