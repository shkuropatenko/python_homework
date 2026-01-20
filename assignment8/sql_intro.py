import sqlite3
# Task 1
# Connect to a new SQLite database
try:
  with sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully.")
except sqlite3.Error as e:
  print(f"An error occurred: {e}")