import sqlite3
import functools

#### decorator to lof SQL queries

def log_queries(func):
  def logger(*args, **kwargs):
    query = ''
    if args:
      query = args[0]
    else:
      query = kwargs.get("query")
    print(F"({query})")
    result = func(*args, **kwargs)
    return result
  return logger

@log_queries
def fetch_all_users(query):
  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  cursor.execute(query)
  results = cursor.fetchall()
  conn.close()
  return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
      
