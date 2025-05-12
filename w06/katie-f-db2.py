# Katie Fournier
# CS 162 Week 06
# SQLite3 Database 2


import sqlite3
from pathlib import Path


def create_artists_table(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute( """--sql
        CREATE TABLE music_artists (artist text, genre text, number_recordings integer)""")
    cursor.executemany( """--sql
        INSERT INTO music_artists VALUES (?, ?, ?)""",
        [   ('Miley', 'Rock', 14),
            ('Dolly', 'Country', 123),
            ('Eminem', 'HipHop', 98),
            ('Brittany', 'Rock', 37)
        ]
    )
    connection.commit()


def create_genres_table(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute("""--sql
        CREATE TABLE genres (genre text, city text)""")
    cursor.executemany("""--sql
        INSERT INTO genres VALUES (?,?) """,
        [  ('Rock', 'Los Angeles'),
           ('Hippie', 'Eugene'),
           ('Opera', 'Florence')
        ]
    )
    connection.commit()


def create_cities_table(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute("""--sql
        CREATE TABLE cities (city text, state text, zip_code integer, population integer)""")
    cursor.executemany("""---sql
        INSERT INTO cities VALUES (?,?,?,?)""",
        [   ('Los Angeles', 'CA', 66666, 10_000_000),
            ('Eugene', 'OR', 55555, 80_000),
            ('Nashville', 'TN', 11111, 1_500_000)
        ]
    )
    connection.commit()


def main():

    # Create the database file
    db_file = "db2.db"
    # Delete any old database file
    Path(db_file).unlink(missing_ok = True)
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    create_artists_table(connection, cursor)
    create_genres_table(connection, cursor)
    create_cities_table(connection, cursor)

    for genre in cursor.execute("SELECT * FROM genres"):
        print(genre)
    print()
    artists_genres = cursor.execute("""--sql
        SELECT ma.artist
        FROM music_artists as ma
        JOIN genres as g
            ON ma.genre = g.genre""")
    for artist in artists_genres:
        print(artist)

    # Take the name of an artist from user input and print info about that artist
    print()
    artist = input('Which artist would you like to know more about? ')
    if artist == "":
        raise ValueError('artist must not be an empty string')
    artist_info = list(cursor.execute("""--sql
        SELECT ma.genre, ma.artist, ma.number_recordings, g.city, c.population
        FROM music_artists AS ma
        FULL JOIN genres AS g
            ON ma.genre = g.genre
        FULL JOIN cities AS c
            ON g.city = c.city
        WHERE ma.artist = ?""",
        (artist.capitalize(),)
    ))

    num_results = len(artist_info)
    if num_results == 0:
        raise Exception(f"database does not contain the artist '{artist}'")
    elif num_results > 1:
        raise Exception(f"expected 1 result for '{artist}' but got {num_results}")
    genre, artist, number_recordings, city, population = artist_info[0]

    result_statement = f"{genre} artist {artist} has {number_recordings:,} recordings and is "

    if city is not None and population is not None:
        result_statement += f"most popular in {city} with a population of {population:,}"
    else:
        result_statement += "popular everywhere"

    print(result_statement)


if __name__ == "__main__":
    main()



