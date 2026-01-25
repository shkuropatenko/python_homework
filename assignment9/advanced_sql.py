import sqlite3

DB_PATH = "../db/lesson.db"

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        print("Connected to DB:", DB_PATH)

        print("\n--- total price of each of the first 5 orders ---")
        
        cursor.execute("""
          SELECT o.order_id, SUM(p.price * li.quantity) AS total_price
          FROM orders o
          JOIN line_items li ON o.order_id = li.order_id
          JOIN products p ON li.product_id = p.product_id
          GROUP BY o.order_id
          ORDER BY o.order_id
          LIMIT 5;
        """)
        
        for row in cursor.fetchall():
            print(row)

        print("\n--- AVG price of each of the first 5 orders ---")
        cursor.execute("""
          SELECT
              c.customer_name,
              AVG(t.total_price) AS average_total_price
          FROM customers c
          LEFT JOIN (
              SELECT
                  o.customer_id AS customer_id_b,
                  SUM(p.price * li.quantity) AS total_price
              FROM orders o
              JOIN line_items li ON o.order_id = li.order_id
              JOIN products p ON li.product_id = p.product_id
              GROUP BY o.order_id
          ) t ON c.customer_id = t.customer_id_b
          GROUP BY c.customer_id
          LIMIT 5;
      """)

        for row in cursor.fetchall():
            print(row)







except sqlite3.Error as e:
    print("DB error:", e)
