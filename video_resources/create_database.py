import sqlite3
db = sqlite3.connect('example.db')

# DDL: Create the Database Structure
db.executescript("""
drop table if exists country;
create table country (
  id integer primary key autoincrement,
  name text not null
);

drop table if exists author;
create table author (
  id integer primary key autoincrement,
  country_id integer,
  name text not null
);

drop table if exists book;
create table book (
  id integer primary key autoincrement,
  author_id integer,
  title text not null,
  isbn text
);
""")

# DML: Insert Countries
db.executescript("""
INSERT INTO country (id, name) VALUES (1, 'United Kingdom');
INSERT INTO country (id, name) VALUES (2, 'USA');
INSERT INTO country (id, name) VALUES (3, 'Republic of Ireland');
""")

# DML: Insert Authors
db.executescript("""
INSERT INTO author (id, country_id, name) VALUES (1, 2, 'Mark Twain');
INSERT INTO author (id, country_id, name) VALUES (2, 3, 'Oscar Wilde');
INSERT INTO author (id, country_id, name) VALUES (3, 1, 'George Orwell');

""")

# DML: Insert Books
db.executescript("""
INSERT INTO book (id, author_id, title, isbn) VALUES (1, 3, '1984', 'XYZ-1');
INSERT INTO book (id, author_id, title, isbn) VALUES (2, 2, 'The Happy Prince', 'XYZ-2');
INSERT INTO book (id, author_id, title, isbn) VALUES (3, 2, 'The Picture of Dorian Gray', 'XYZ-3');
INSERT INTO book (id, author_id, title, isbn) VALUES (4, 1, 'The Adventures of Tom Sawyer', 'XYZ-4');
INSERT INTO book (id, author_id, title, isbn) VALUES (5, 1, 'The Adventures of Huckleberry Finn', 'XYZ-5');
INSERT INTO book (id, author_id, title, isbn) VALUES (6, 2, 'The Canterville Ghost', 'XYZ-6');
INSERT INTO book (id, author_id, title, isbn) VALUES (7, 3, 'Animal Farm', 'XYZ-7');
""")
