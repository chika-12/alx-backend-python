import sqlite3

def stream_users():
    conn = sqlite3.connect('ALX_prodev')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()


    cur = cursor.execute("SELECT * FROM user_data")
    try:
        for row in cur:
            yield dict(row)
    finally:
        cur.close()
        conn.close()

