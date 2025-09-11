import sqlite3
from contextlib import contextmanager

database_name = "../python-generators-0x00/ALX_prodev"

@contextmanager
def database(db_name, query):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        yield cursor.fetchall()
        conn.commit()
    except: 
        conn.rollback()
    finally:
        conn.close()
with database(database_name, "SELECT * FROM users;") as data:
    for val in data:
        print(dict(val))



