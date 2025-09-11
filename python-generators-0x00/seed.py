#!/usr/bin/python3
"""A python script for database management"""
import sqlite3
import csv
import os
import uuid

#db configuration
DB_NAME = "ALX_prodev"
DB_USER = "postgres"   
DB_PASS = "chika"           
DB_HOST = "127.0.0.1"  
DB_PORT = 5432 

def connect_db(dbname="DB_USER"):
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_database(connection):
    """Creates the SQLite database file if it does not exist."""
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        conn.close()
        print(f"Database {DB_NAME} created.")
    else:
        print(f"Database {DB_NAME} already exists.")

def connect_to_prodev():
    """Connects to data base"""
    return connect_db(DB_NAME)


def create_table(connection):
     """Creates the user_data table if it does not exist."""
     cur = connection.cursor()
     cur.execute("""
     CREATE TABLE IF NOT EXISTS user_data (
     user_id TEXT PRIMARY KEY,
     name VARCHAR NOT NULL,
     email VARCHAR NOT NULL UNIQUE,
     age DECIMAL NOT NULL
     );
  """)
     connection.commit()
     cur.close()
     print("Table user_data ready.")

def insert_data(connection, data):
    """Insert data into table"""
    cur = connection.cursor()
    if not os.path.exists(data):
        raise FileNotFoundError(f"{data} not found")
    with open(data, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("""
            INSERT OR IGNORE INTO user_data (user_id, name, email, age)
            VALUES (?, ?, ?, ?);
            """, (str(uuid.uuid4()), row["name"], row["email"], row["age"]))
    connection.commit()
    cur.close()
    print("data loaded successfully")



