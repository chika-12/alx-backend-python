import sqlite3

def stream_users():
    conn = sqlite3.connect('ALX_prodev')
    cursor = conn.cursor()

    cur = cursor.execute("SELECT * FROM user_data")
    try:
        for row in cur:
            yield row
    finally:
        cur.close()
        conn.close()

