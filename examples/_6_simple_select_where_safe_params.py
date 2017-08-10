import sqlite3

db = sqlite3.connect('library_simple.db')

# American Authors
query = "SELECT * FROM author WHERE country_id = :country_id"

params = {
    'country_id': 1  # Try the SQL Injection
}

cursor = db.execute(query, params)
for row in cursor:
    print("{} - {}".format(row[0], row[2]))
