import sqlite3

def add_publisher(cursor, name):
  try:
    cursor.execute("INSERT INTO publishers (name) VALUES (?);", (name,))
  except sqlite3.IntegrityError:
    pass

def add_magazine(cursor, name, publisher_id):
  try:
    cursor.execute(
      "INSERT INTO magazines (name, publisher_id) VALUES (?, ?);",
      (name, publisher_id)
    )
  except sqlite3.IntegrityError:
    pass

def add_subscriber(cursor, name, address, email):
  cursor.execute(
    "SELECT id FROM subscribers WHERE name = ? AND address = ?;",
    (name, address)
  )
  if cursor.fetchone() is not None:
    return

  try:
    cursor.execute(
      "INSERT INTO subscribers (name, address, email) VALUES (?, ?, ?);",
      (name, address, email)
    )
  except sqlite3.IntegrityError:
    pass

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
  try:
    cursor.execute(
      """
      INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
      VALUES (?, ?, ?);
      """,
      (subscriber_id, magazine_id, expiration_date)
    )
  except sqlite3.IntegrityError:
    pass

try:
  with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 2: Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL UNIQUE,
      publisher_id INTEGER NOT NULL,
      FOREIGN KEY (publisher_id) REFERENCES publishers(id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      address TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
      id INTEGER PRIMARY KEY,
      subscriber_id INTEGER NOT NULL,
      magazine_id INTEGER NOT NULL,
      expiration_date TEXT,
      FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
      FOREIGN KEY (magazine_id) REFERENCES magazines(id),
      UNIQUE (subscriber_id, magazine_id)
    )
    """)


    # Task 3: Insert data
    # publishers
    for p in ["Condé Nast", "Hearst", "Time Inc."]:
      add_publisher(cursor, p)

    cursor.execute("SELECT id FROM publishers WHERE name = ?;", ("Condé Nast",))
    conde_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM publishers WHERE name = ?;", ("Hearst",))
    hearst_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM publishers WHERE name = ?;", ("Time Inc.",))
    time_id = cursor.fetchone()[0]

    mags = [("Vogue", conde_id), ("Cosmopolitan", hearst_id), ("Time", time_id)]
    for name, pub_id in mags:
      add_magazine(cursor, name, pub_id)

    subs = [
      ("Alex Kim", "12 Main St, NY", "alex1@example.com"),
      ("Alex Kim", "99 Broadway, NY", "alex2@example.com"),
      ("Maria Lopez", "5 Pine Rd, NY", "maria@example.com"),
    ]
    for name, address, email in subs:
      add_subscriber(cursor, name, address, email)

    cursor.execute("SELECT id FROM subscribers WHERE email = ?;", ("alex1@example.com",))
    alex_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM subscribers WHERE email = ?;", ("alex2@example.com",))
    alex2_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM subscribers WHERE email = ?;", ("maria@example.com",))
    maria_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM magazines WHERE name = ?;", ("Vogue",))
    vogue_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM magazines WHERE name = ?;", ("Cosmopolitan",))
    cosmo_id = cursor.fetchone()[0]
    cursor.execute("SELECT id FROM magazines WHERE name = ?;", ("Time",))
    time_mag_id = cursor.fetchone()[0]

    add_subscription(cursor, alex_id, vogue_id, "2025-12-31")
    add_subscription(cursor, alex_id, cosmo_id, "2025-10-01")
    add_subscription(cursor, maria_id, time_mag_id, "2026-01-15")

    conn.commit()

    # Task 4: Queries
    print("\nAll subscribers:")
    cursor.execute("SELECT * FROM subscribers;")
    for row in cursor.fetchall():
      print(row)

    print("\nAll magazines sorted by name:")
    cursor.execute("SELECT * FROM magazines ORDER BY name;")
    for row in cursor.fetchall():
      print(row)

    print("\nMagazines published by Condé Nast:")
    cursor.execute("""
      SELECT m.id, m.name
      FROM magazines m
      JOIN publishers p ON m.publisher_id = p.id
      WHERE p.name = ?;
    """, ("Condé Nast",))
    for row in cursor.fetchall():
      print(row)

except sqlite3.Error as e:
  print(f"An error occurred: {e}")