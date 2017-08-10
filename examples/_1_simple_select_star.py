import sqlite3

db = sqlite3.connect('library_simple.db')

cursor = db.execute("SELECT * FROM author")

print("Authors:")
for row in cursor:
    print(row)
