import sqlite3

DB_PATH = "../db/lesson.db"

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        print("Connected to DB:", DB_PATH)

        print("\n--- Task1: total price of each of the first 5 orders ---")
        
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

        print("\n---Task 2: total price of each of the first 5 orders ---")
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

        print("\n--- Task 3: Insert order in ONE transaction ---")
        try:
            conn.execute("BEGIN")  # start transaction

            # 1) insert order, get new order_id
            cursor.execute("""
                INSERT INTO orders (customer_id, employee_id, date)
                VALUES (?, ?, DATE('now'))
                RETURNING order_id;
            """, (16, 7))
            new_order_id = cursor.fetchone()[0]
            print("Created order_id:", new_order_id)

            # 2) insert 5 line_items (qty=10 each)
            product_ids = [23, 18, 43, 9, 44]
            for pid in product_ids:
                cursor.execute("""
                    INSERT INTO line_items (order_id, product_id, quantity)
                    VALUES (?, ?, ?);
                """, (new_order_id, pid, 10))

            conn.commit()  # commit transaction

        except Exception as e:
            conn.rollback()
            print("Rolled back. Error:", e)
            raise

        # 3) verify with SELECT + JOIN
        print("\nLine items created for this order:")
        cursor.execute("""
            SELECT li.line_item_id, li.quantity, p.product_name
            FROM line_items li
            JOIN products p ON li.product_id = p.product_id
            WHERE li.order_id = ?
            ORDER BY li.line_item_id;
        """, (new_order_id,))

        for row in cursor.fetchall():
            print(row)



except sqlite3.Error as e:
    print("DB error:", e)
