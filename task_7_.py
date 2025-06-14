# -*- coding: utf-8 -*-
"""Task 7 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13LjEQxWbklfu4S-R1A71xoLUeLb4wFC9
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load SQLite database
conn = sqlite3.connect("sales_data.db")

# Create and populate table (only for demo/test purposes)
conn.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')
conn.executemany('''
INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)
''', [
    ('Product A', 10, 20.0),
    ('Product B', 5, 30.0),
    ('Product A', 7, 20.0),
    ('Product C', 3, 50.0),
    ('Product B', 8, 30.0)
])
conn.commit()

# View full table
print("All Sales Records:")
df_all = pd.read_sql_query("SELECT * FROM sales", conn)
print(df_all)

# Run basic SQL summary
query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"

# Load into pandas
df = pd.read_sql_query(query, conn)

# Print results
print("\nSummary of Sales:")
print(df)

# Plot simple bar chart
df.plot(kind='bar', x='product', y='revenue')
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()

# Save chart if needed
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close the connection
conn.close()