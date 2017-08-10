import sqlite3

db = sqlite3.connect('library_simple.db')

print("Before Deleting:")

cursor = db.execute("SELECT * FROM book")
for row in cursor:
    print(row)

query = "DELETE FROM book;"
cursor = db.execute(query)
db.commit()


cursor = db.execute("SELECT * FROM book")
print("After Deleting:")

for row in cursor:
    print(row)
