# load_pets.py
import sqlite3

def load_data():
    # Connect to or create the database
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER,
        pet_id INTEGER
    );
    """)

    # Insert data into person
    people = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]
    cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?);", people)

    # Insert data into pet
    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]
    cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?);", pets)

    # Insert data into person_pet
    person_pets = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]
    cursor.executemany("INSERT INTO person_pet VALUES (?, ?);", person_pets)

    conn.commit()
    conn.close()
    print("✅ pets.db created and data loaded successfully!")

if __name__ == "__main__":
    load_data()

