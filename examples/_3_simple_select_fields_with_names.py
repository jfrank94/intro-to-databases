import sqlite3

db = sqlite3.connect('library_simple.db')

# Row Factory:
db.row_factory = sqlite3.Row

cursor = db.execute("SELECT id, name FROM author")

print("Authors:")
for row in cursor:
    print("{id} - {name}".format(id=row['id'], name=row['name']))
