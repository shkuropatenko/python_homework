import sqlite3

DB_PATH = "../db/lesson.db"

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        print("Connected to DB:", DB_PATH)

        # cursor.execute("""
        #   SELECT order_id,
        #   FROM orders
        #   JOIN Students ON Enrollments.student_id = Students.student_id
        #   JOIN Courses ON Enrollments.course_id = Courses.course_id;
        # """)

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






except sqlite3.Error as e:
    print("DB error:", e)
