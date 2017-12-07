import sqlite3
from pprint import pprint

db = sqlite3.connect('example.db')

TITLE = "Iterating the cursor"
print("\n==== {:^70} ====".format(TITLE))
cursor = db.execute('SELECT id, author_id, title, isbn FROM book;')
for book in cursor:
    book_id, author_id, title, isbn = book
    print('({}) {:<50} by {} - [{}]'.format(
        book_id, title, author_id, isbn))
print('=' * 80)

TITLE = "Fetching a single object"
print("\n==== {:^70} ====".format(TITLE))
cursor = db.execute('SELECT id, author_id, title, isbn FROM book;')
print(cursor.fetchone())
print('=' * 80)

TITLE = "Fetching all the objects"
print("\n==== {:^70} ====".format(TITLE))
cursor = db.execute('SELECT id, author_id, title, isbn FROM book;')
pprint(cursor.fetchall())
print('=' * 80)

TITLE = "Fetching many objects"
print("\n==== {:^70} ====".format(TITLE))
cursor = db.execute('SELECT id, author_id, title, isbn FROM book;')
pprint(cursor.fetchmany(3))
print('=' * 80)
