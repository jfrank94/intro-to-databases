import sqlite3

db = sqlite3.connect('library_constraints.db')
db.execute("PRAGMA foreign_keys = 1")  # Important

cursor = db.execute("DELETE FROM country WHERE id = 1")

db.commit()
