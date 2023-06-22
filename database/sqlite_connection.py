import json
import sqlite3

with open('data.json') as f:
    data = json.load(f)

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

for record in data:
    cursor.execute('''
        INSERT INTO my_table (id, name, age)
        VALUES (?, ?, ?)
    ''', (record['id'], record['name'], record['age']))

conn.commit()
conn.close()