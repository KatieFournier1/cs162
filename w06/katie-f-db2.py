# Katie Fournier
# CS 162 Week 06
# SQLite3 Database 2


import sqlite3
from pathlib import Path


def create_artists_table(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute("""--sql
        CREATE TABLE music_artists (artist text, genre text, number_recordings integer)
        """
    )
    cursor.executemany("""--sql
        INSERT INTO music_artists VALUES (?, ?, ?)
        """,
        [   ('Miley', 'Rock', 14),
            ('Dolly', 'Country', 123),
            ('Eminem', 'HipHop', 98),
            ('Brittany', 'Rock', 37)
        ]
    )
    connection.commit()


def create_genres_table(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute("""--sql
        CREATE TABLE genres (genre text, city text)
        """
    )
    cursor.executemany("""--sql
        INSERT INTO genres VALUES (?,?)
        """,
        [  ('Rock', 'Los Angeles'),
           ('Hippie', 'Eugene'),
           ('Opera', 'Florence')
        ]
    )
    connection.commit()


def create_cities_table(connection: sqlite3.Connection, cursor: sqlite3.Cursor) -> None:
    cursor.execute("""--sql
        CREATE TABLE cities (city text, state text, zip_code integer, population integer)
        """
    )
    cursor.executemany("""---sql
        INSERT INTO cities VALUES (?,?,?,?)
        """,
        [   ('Los Angeles', 'CA', 66666, 10_000_000),
            ('Eugene', 'OR', 55555, 80_000),
            ('Nashville', 'TN', 11111, 1_500_000)
        ]
    )
    connection.commit()



def main():
    # create the database file
    db_file = "db2.db"
    db_path = Path(db_file)
    # Make sure we are starting with an empty database file
    if db_path.exists():
        print("Deleted db2.db\n")
    Path(db_file).unlink(missing_ok = True)
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    create_artists_table(connection, cursor)
    create_genres_table(connection, cursor)
    create_cities_table(connection, cursor)

    artists_in_genre_table = list(cursor.execute("""--sql
        SELECT artist
        FROM music_artists AS ma
        JOIN genres AS g
            ON ma.genre = g.genre
        """
    ))

    for genre in cursor.execute("SELECT * FROM genres"):
        print(genre)
    print()
    for artist in artists_in_genre_table:
        print(artist)

    print()
    lookup_artist__raw__ = input('Which artist would you like to know more about? ')
    if lookup_artist__raw__ == "":
        raise ValueError('artist must not be an empty string')
    lookup_artist = (lookup_artist__raw__.capitalize(),)

    artist_is_in_genre_table = lookup_artist in artists_in_genre_table
    if artist_is_in_genre_table:
        artist_query = """--sql
            SELECT ma.genre, ma.artist, ma.number_recordings, g.city, c.population
            FROM music_artists AS ma
            JOIN genres AS g
                ON ma.genre = g.genre
            JOIN cities AS c
                ON g.city = c.city
            WHERE ma.artist = ?
            """
    else:
        artist_query = """--sql
            SELECT ma.genre, ma.artist, ma.number_recordings
            FROM music_artists AS ma
            WHERE ma.artist = ?
            """
    artist_query_results = list(cursor.execute(artist_query, lookup_artist))

    num_results = len(artist_query_results)
    if num_results == 0:
        raise Exception(f"database does not contain the artist '{lookup_artist__raw__}'")
    elif num_results > 1:
        raise Exception(f"expected 1 result for '{lookup_artist__raw__}' but got {num_results}")
    artist_info = artist_query_results[0]

    genre, artist, number_recordings = artist_info[0:3]
    result_statement = f"{genre} artist {artist} has {number_recordings:,} recordings and is "

    if artist_is_in_genre_table:
        city, population = artist_info[3:5]
        result_statement += f"most popular in {city} with a population of {population:,}"
    else:
        result_statement += "popular everywhere"

    print(result_statement)


if __name__ == "__main__":
    main()



