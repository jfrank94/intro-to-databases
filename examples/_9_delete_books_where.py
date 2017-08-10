import sqlite3

db = sqlite3.connect('library_simple.db')


query = """INSERT INTO book (
    author_id, title, isbn
) VALUES (
    :author_id, :title, :isbn
);"""

cursor = db.execute(query, {
    'title': 'The Raven',
    'author_id': 1,
    'isbn': 'TR1'
})
cursor = db.execute(query, {
    'title': 'The Facts in the Case of M. Valdemar',
    'author_id': 1,
    'isbn': 'TFV2'
})


print("Before Deleting:")

cursor = db.execute("SELECT * FROM book")
for row in cursor:
    print(row)

# Deleting Books
cursor = db.execute("DELETE FROM book WHERE isbn = :isbn", {
    'isbn': 'TFV2'
})
db.commit()

print("After Deleting:")
cursor = db.execute("SELECT * FROM book")
for row in cursor:
    print(row)
