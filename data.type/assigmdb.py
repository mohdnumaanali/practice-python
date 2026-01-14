import csv
import sqlite3
import os

# Remove old database to start fresh
if os.path.exists('tracks.sqlite'):
    os.remove('tracks.sqlite')

# Connect to SQLite database
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# Drop and create tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
);
''')

# Read CSV file using positional columns
with open('D:/practice-python/data.type/tracks.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)

    for row in reader:
        if len(row) != 7:
            continue  # skip malformed rows

        track = row[0]
        artist = row[1]
        album = row[2]
        length = row[3]
        rating = row[4]
        count = row[5]
        genre = row[6]

        if not (track and artist and album and genre):
            continue

        # Insert Artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert Genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert Album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # Insert Track
        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (track, album_id, genre_id, length, rating, count))

# Save and close
conn.commit()
conn.close()

print("✅ Database created successfully: tracks.sqlite")
