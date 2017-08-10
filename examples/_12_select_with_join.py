import sqlite3

db = sqlite3.connect('library_simple.db')
db.row_factory = sqlite3.Row

# American Authors
query = """
SELECT a.id as id, a.name as name, c.name as country
FROM author a INNER JOIN country c ON a.country_id = c.id;
"""


cursor = db.execute(query)
for row in cursor:
    print("{} - {} - {}".format(row['id'], row['name'], row['country']))
