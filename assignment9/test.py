import sqlite3

DB_PATH = "../db/school.db"

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        print("Connected to DB:", DB_PATH)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary INTEGER NOT NULL,
            department TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        );
        """)

        # Insert Employees (simple)
        cursor.execute("""
        INSERT OR IGNORE INTO Employees (id, name, salary, department)
        VALUES
            (1, 'Alice', 80000, 'IT'),
            (2, 'Bob', 60000, 'IT'),
            (3, 'Charlie', 72000, 'HR'),
            (4, 'Diana', 50000, 'HR'),
            (5, 'Evan', 95000, 'Finance');
        """)

        # Insert Projects (simple)
        cursor.execute("""
        INSERT OR IGNORE INTO Projects (id, name, department)
        VALUES
            (1, 'Project A', 'HR'),
            (2, 'Project B', 'IT'),
            (3, 'Project C', 'Finance');
        """)

        conn.commit()
        print("Sample data inserted.")

        print("\n--- GROUP BY: avg salary per department ---")
        cursor.execute("""
        SELECT department, AVG(salary) AS avg_salary
        FROM Employees
        GROUP BY department;
        """)
        for row in cursor.fetchall():
            print(row)

        print("\n--- HAVING: departments with avg salary > 70000 ---")
        cursor.execute("""
        SELECT department, AVG(salary) AS avg_salary
        FROM Employees
        GROUP BY department
        HAVING AVG(salary) > 70000;
        """)
        for row in cursor.fetchall():
            print(row)

        print("\n--- JOIN: projects for high-paying departments!!!!!!! ---")
        cursor.execute("""
        SELECT p.name AS project_name, p.department
        FROM Projects p
        JOIN (
            SELECT department
            FROM Employees
            GROUP BY department
            HAVING AVG(salary) > 70000
        ) hi ON hi.department = p.department;
        """)
        for row in cursor.fetchall():
            print(row)

        print("\n--- SUBQUERY: projects where department is in high-paying list ---")
        cursor.execute("""
        SELECT name, department
        FROM Projects
        WHERE department IN (
            SELECT department
            FROM Employees
            GROUP BY department
            HAVING AVG(salary) > 70000
        );
        """)
        for row in cursor.fetchall():
            print(row)





except sqlite3.Error as e:
    print("DB error:", e)
