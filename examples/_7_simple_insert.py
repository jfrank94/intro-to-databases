import sqlite3

db = sqlite3.connect('library_simple.db')

# We get this from the user for example:
title = 'The Raven'
isbn = '321'
author_id = 1


query = """INSERT INTO book (
    author_id, title, isbn
) VALUES (
    :author_id, :title, :isbn
);"""

cursor = db.execute(query, {
    'title': title,
    'author_id': author_id,
    'isbn': isbn
})

db.commit()


cursor = db.execute("SELECT * FROM book")

print("Books:")
for row in cursor:
    print(row)
