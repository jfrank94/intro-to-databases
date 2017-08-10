import sqlite3

db = sqlite3.connect('library_constraints.db')
db.execute("PRAGMA foreign_keys = 1")  # Important


query = """INSERT INTO book (
    author_id, title, isbn
) VALUES (
    :author_id, :title, :isbn
);"""


cursor = db.execute(query, {
    'title': 'The Raven',
    'author_id': 100, # Author doesn't exist
    'isbn': 'TR1'
})


db.commit()
