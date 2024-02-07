from config import CONN, CURSOR
import sqlite3

conn = sqlite3.connect('music.db')
CURSOR = conn.cursor()

class Song:

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
    def save(self):
            sql = "INSERT INTO songs (name, album) VALUES (?, ?)"
            with sqlite3.connect('music.db') as conn:
                cursor = conn.cursor()
                cursor.execute(sql, (self.name, self.album))
                conn.commit()


    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        # After saving the song, retrieve its id from the database
        db_song = CURSOR.execute(
            'SELECT * FROM songs WHERE name=? AND album=?',
            (name, album)
        ).fetchone()
        song.id = db_song[0]  # Assign the id retrieved from the database to the song instance
        return song