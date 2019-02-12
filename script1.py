import sqlite3


def create_table():
    # connect to a database file
    conn = sqlite3.connect("lite.db")

    # create cursor object
    cur = conn.cursor()

    # SQL code
    cur.execute("CREATE TABLE IF NOT EXISTS store (item MESSAGE_TEXT , quantity INTEGER, price REAL)")  # useSQLkeywords
    cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# add data
def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit()
    conn.close()


insert_data("Coffee Cup", 10, 5)


# View data
def view_data():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")  # * means all
    rows = cur.fetchall()
    conn.close()
    return rows


print(view_data())


# Delete Data
def delete_data(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


delete_data("Wine Glass")
# print(view_data())


# Update data
def update_data(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()


update_data(11, 6, "Water Glass")
# print(view_data())

