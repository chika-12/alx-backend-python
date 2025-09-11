import sqlite3

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.cursor = None
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
        self.conn.close()


with Database("../python-generators-0x00/ALX_prodev") as cur:
    cur.execute("SELECT * FROM users;")
    data = cur.fetchall()
    for val in data:
       #if val['age'] > 90:
       print(dict(val))


