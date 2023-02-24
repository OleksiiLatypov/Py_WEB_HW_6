import sqlite3
from contextlib import contextmanager

database = './homework.db'


@contextmanager
def connect(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()