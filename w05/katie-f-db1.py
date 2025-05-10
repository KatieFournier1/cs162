# Katie Fournier
# CS 162 Week 05
# SQLite3 Database 1


import sqlite3
from pathlib import Path


def main():
    db_file = "db1.db"
    # Make sure we are starting with an empty database file
    Path(db_file).unlink(missing_ok = True)

    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE music_artists
            (artist text, genre text, number_recordings integer)
    """)
    music_artists = [
        ('Miley', 'Rock', 14),
        ('Dolly', 'Country', 123),
        ('Eminen', 'HipHop', 98),
        ('Brittany', 'Rock', 37)
    ]
    cursor.executemany("INSERT INTO music_artists VALUES (?, ?, ?)", music_artists)
    connection.commit()

    for row in cursor.execute("SELECT * FROM music_artists WHERE genre = ?", ("Rock",)):
        print(row)


if __name__ == "__main__":
    main()
