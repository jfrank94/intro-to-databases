import sqlite3

db = sqlite3.connect('library_simple.db')

# American Authors
query = "SELECT * FROM author WHERE country_id = %s"

country_id = "1 or 1 == 1"  # We're getting this from an untrusted source

cursor = db.execute(query % country_id)
for row in cursor:
    print("{} - {}".format(row[0], row[2]))

print("We read the entire TABLE!")
