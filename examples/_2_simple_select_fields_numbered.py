import sqlite3

db = sqlite3.connect('library_simple.db')

cursor = db.execute("SELECT id, name FROM author")

print("Authors:")
for row in cursor:
    print("{id} - {name}".format(id=row[0], name=row[1]))
