import sqlite3
from itertools import islice, chain

def stream_users_in_batches(batch_size):
    conn = sqlite3.connect("ALX_prodev")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    #new_curr = conn.cursor()
    
    cur = cursor.execute("SELECT * FROM user_data;")
    #count = len(cur.description)
    
    while True:
        data = cur.fetchmany(batch_size)
        if not data:
            break;
        else:
            for row in data:
                yield dict(row)
    cur.close()
    conn.close()




def batch_processing(batch_size):
    for data in stream_users_in_batches(batch_size):
        if data['age'] > 25:
            print(data)




#for data in islice(stream_users_in_batches(10), 2):
 #   print(data)
