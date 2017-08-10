-- sqlite3 library_simple.db < schemas/simple-library.sql

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

-- Initial Data:

-- Countries
INSERT INTO country (id, name) VALUES (1, 'US');
INSERT INTO country (id, name) VALUES (2, 'England');
INSERT INTO country (id, name) VALUES (3, 'Argentina');
INSERT INTO country (id, name) VALUES (4, 'Scotland');

-- Authors
INSERT INTO author (id, country_id, name) VALUES (1, 1, 'Edgar Allan Poe');
INSERT INTO author (id, country_id, name) VALUES (2, 1, 'Mark Twain');
INSERT INTO author (id, country_id, name) VALUES (3, 4, 'Arthur Conan Doyle');
INSERT INTO author (id, country_id, name) VALUES (4, 3, 'Jorge Luis Borges');
