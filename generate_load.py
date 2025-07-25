import random
import time
import os

import pandas as pd
from sqlalchemy import create_engine

DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
DB_NAME = os.getenv("POSTGRES_DB", "chinook")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")


def main():
    """A script to generate and insert random track data into the 'Track' table of the Chinook database.

    Reads track names and composers from a CSV file, generates random track information,
    and inserts it into the database table indefinitely.

    This script connects to the Chinook database and continuously inserts new track records
    with random data into the 'Track' table. It uses a CSV file containing track names and composers
    and generates random values for other track attributes such as genre, milliseconds, bytes, and unit price.
    """
    # read chinook track data from CSV
    track_df = pd.read_csv("/tmp/track.csv", usecols=["Name", "Composer"])

    # connect to database
    print("connecting to DB")
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    conn = engine.connect()

    # fetch largest track id
    res = conn.execute("""SELECT COALESCE(MAX("TrackId"), 0) FROM "Track" """).fetchall()
    track_id = res[0][0]

    while True:
        track_rand_id = random.randrange(2, 3000)
        track_name = track_df.iloc[track_rand_id, 0]
        track_genre = random.randrange(1, 5)
        track_composer = track_df.iloc[track_rand_id, 1]
        track_milliseconds = random.randrange(100000, 300000)
        track_bytes = random.randrange(100000, 500000)
        track_id += 1

        insert_stmt = """INSERT INTO public."Track"
                ("TrackId", "Name", "AlbumId", "MediaTypeId", "GenreId", "Composer", "Milliseconds", "Bytes", "UnitPrice")
                VALUES (%s, %s, 1, 1, %s, %s, %s, %s, 0.99)"""
        conn.execute(insert_stmt, (track_id, track_name, track_genre, track_composer, track_milliseconds, track_bytes))

        print(".", end="", flush=True)
        time.sleep(random.randint(100, 500)/1000)


if __name__ == "__main__":
    main()
