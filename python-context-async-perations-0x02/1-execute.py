#!/usr/bin/python3

import sqlite3
# from contextlib import contextmanager

database_name = "../python-generators-0x00/ALX_prodev"

class ExecuteQuery:
    def __init__(self, db_name, query):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.query = query

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.cursor.execute(self.query)
        return self.cursor.fetchall()

    def __exit__(self, exc_type, exc_val, exc_db):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        self.conn.close()
with ExecuteQuery(database_name, "SELECT * FROM users WHERE age > 89;") as data:
    for row in data:
        print(dict(row))


