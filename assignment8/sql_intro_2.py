import sqlite3
import pandas as pd

DB_PATH = "../db/lesson.db"

SQL = """
SELECT
  li.line_item_id,
  li.quantity,
  li.product_id,
  p.product_name,
  p.price
FROM line_items li
JOIN products p
  ON li.product_id = p.product_id;
"""

try:
  with sqlite3.connect(DB_PATH) as conn:
    # 1 Read JOIN to DataFrame
    df = pd.read_sql_query(SQL, conn)
    print("Raw joined data (first 5):")
    print(df.head())

    # 2 Business logic: total = quantity * price
    df["total"] = df["quantity"] * df["price"]
    print("\nWith total column (first 5):")
    print(df.head())

    # 3 Result - group by product
    summary = (
        df.groupby("product_id", as_index=False)
          .agg({
              "line_item_id": "count",
              "total": "sum",
              "product_name": "first",
          })
    )
    print("\nGrouped summary (first 5):")
    print(summary.head())

    # 4 Sort by name product
    summary = summary.sort_values("product_name")
    summary = summary.rename(columns={"line_item_id": "times_ordered"})

    # 5 Record into CSV
    out_path = "order_summary.csv"
    summary.to_csv(out_path, index=False)
    print(f"\nSaved: {out_path}")

except Exception as e:
    print(f"Error: {e}")
