import sqlite3
def stream_user_ages():
    conn = sqlite3.connect("ALX_prodev")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT age FROM user_data;")
    data = cursor.fetchall()
    for row in data:
        yield dict(row)
    conn.close()

total_age = 0
count = 0
for age_row in stream_user_ages():
    total_age += age_row['age']
    count += 1
avg = total_age / count
print(f"Average age of users: {avg}")
