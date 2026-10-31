import sqlite3

conn = sqlite3.connect('database.db')

cur = conn.cursor()

# customers = [
#     ("John", "Doe", "john.doe@example.com"),
#     ("Jane", "Doe", "jane.doe@example.com"),
#     ("Bob", "Smith", "bob.smith@example.com"),
#     ("Alice", "Johnson", "alice.johnson@example.com"),
#     ("Mike", "Williams", "mike.williams@example.com"),
#     ("Emma", "Davis", "emma.davis@example.com"),
# ]
# cur.executemany("INSERT INTO customers VALUES (?,?,?)", customers)

# cur.execute("""UPDATE customers SET first_name = 'Sushant', last_name = 'Shrestha', email = 'sushant@gmail.com'
#             WHERE rowid = 1
# """)
# conn.commit()

cur.execute("DELETE FROM customers WHERE rowid = 4")
conn.commit()


cur.execute("SELECT rowid,* FROM customers ORDER BY first_name")
customers = cur.fetchall()
for customer in customers:
    print(customer)
    
print("command executed")

conn.commit()
conn.close()