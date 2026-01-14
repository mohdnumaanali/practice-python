# import sqlite3
# -- Create Users table
# CREATE TABLE User (
#     id     INTEGER PRIMARY KEY AUTOINCREMENT,
#     name   TEXT,
#     email  TEXT
# );

# -- Create Courses table
# CREATE TABLE Course (
#     id     INTEGER PRIMARY KEY AUTOINCREMENT,
#     title  TEXT
# );

# -- Create Membership table (junction table)
# CREATE TABLE Member (
#     user_id   INTEGER,
#     course_id INTEGER,
#     role      INTEGER,
#     PRIMARY KEY (user_id, course_id),
#     FOREIGN KEY (user_id) REFERENCES User(id),
#     FOREIGN KEY (course_id) REFERENCES Course(id)
# );

import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Drop old tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')

# Create new tables
cur.executescript('''
CREATE TABLE User (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT,
    email  TEXT
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT
);

CREATE TABLE Member (
    user_id   INTEGER,
    course_id INTEGER,
    role      INTEGER,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES User(id),
    FOREIGN KEY (course_id) REFERENCES Course(id)
);
''')

# Insert sample data
cur.execute('INSERT INTO User (name, email) VALUES (?, ?)', ('Jane', 'jane@tsugi.org'))
cur.execute('INSERT INTO User (name, email) VALUES (?, ?)', ('Ed', 'ed@tsugi.org'))
cur.execute('INSERT INTO User (name, email) VALUES (?, ?)', ('Sue', 'sue@tsugi.org'))

cur.execute('INSERT INTO Course (title) VALUES (?)', ('Python',))
cur.execute('INSERT INTO Course (title) VALUES (?)', ('SQL',))
cur.execute('INSERT INTO Course (title) VALUES (?)', ('PHP',))

# Memberships
cur.execute('INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (1, 1, 1))  # Jane instructor Python
cur.execute('INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (2, 1, 0))  # Ed student Python
cur.execute('INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (3, 1, 0))  # Sue student Python

cur.execute('INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (1, 2, 0))  # Jane student SQL
cur.execute('INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (2, 2, 1))  # Ed instructor SQL

cur.execute('INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (3, 3, 1))  # Sue instructor PHP

conn.commit()

# Query to show roster
sql = '''
SELECT User.name, Member.role, Course.title
FROM User
JOIN Member ON Member.user_id = User.id
JOIN Course ON Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
'''

for row in cur.execute(sql):
    print(row)

cur.close()
