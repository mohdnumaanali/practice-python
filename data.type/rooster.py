import csv
import sqlite3
import os

if os.path.exists('rosterdb.sqlite'):
    os.remove('rosterdb.sqlite')

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

fname = 'D:/practice-python/data.type/roster_data.csv'
with open(fname, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        title = row[1]
        role = int(row[2])

        cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
        cur.execute('SELECT id FROM User WHERE name = ?', (name,))
        user_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
        cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
        course_id = cur.fetchone()[0]

        cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)',
                    (user_id, course_id, role))

conn.commit()
conn.close()
