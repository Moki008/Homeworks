import sqlite3

def create_connection(db_file):
    conn = None
    try:
        with db_file.connect() as conn:
            conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(db_file, create_table_sql):
    try:
        with db_file.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)
    return conn

def set_product(db_file, product):
    set_prod = """INSERT INTO products (
    product_title, price, quantity) 
    VALUES (?,?,?)"""
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(set_prod, product)
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

sql_create_products_table = """
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(10, 2) NOT NULL,
quantity INT NOT NULL DEFAULT 0
)"""
db_name = "hw.db"

# db_name2 = create_connection(db_name1)
# if db_name2 is not None:
#     print("Connection successful")
#     # create_table(db_name2, sql_create_products_table)
#     db_name2.close()

# set_product(db_name, ('Smartphone', 100, 50))
# set_product(db_name, ('Computer', 2000, 20))
# set_product(db_name, ('PS 4', 200, 70))
# set_product(db_name, ('PS 5', 350, 45))
# set_product(db_name, ('TV', 500, 150))
# set_product(db_name, ('Air Pods', 20, 500))
# set_product(db_name, ('Powerbank', 20, 500))
# set_product(db_name, ('Apple watch', 75, 300))
# set_product(db_name, ('Changer', 5, 1000))
# set_product(db_name, ('Case', 2, 2000))
# set_product(db_name, ('Bag', 15, 500))
# set_product(db_name, ('Book', 10, 450))
# set_product(db_name, ('Pen', 1, 1500))
# set_product(db_name, ('Notepad', 5, 500))
# set_product(db_name, ('Ps 3', 120, 80))

def change_quantity(db_file, product):
    change_quantity_sql = "UPDATE products SET quantity = ? WHERE id = ?"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(change_quantity_sql, product)
            conn.commit()
    except sqlite3.Error as e:
        print(e)

# change_quantity(db_name, (60, 1))

def change_price(db_file, product):
    change_quantity_sql = "UPDATE products SET price = ? WHERE id = ?"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(change_quantity_sql, product)
            conn.commit()
    except sqlite3.Error as e:
        print(e)

# change_price(db_name, (150, 1))

def delete_product(db_file, product):
    delete_product_sql = "DELETE FROM products WHERE id = ?"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(delete_product_sql, product)
            conn.commit()
            print("Product deleted")
    except sqlite3.Error as e:
        print(e)

# delete_product(db_name, (15,))

def get_products(db_file):
    get_sql = "SELECT * FROM products"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(get_sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print(e)

# get_products(db_name)

def select_products_by_price(db_file):
    select_sql = "SELECT * FROM products WHERE price < 100 AND quantity > 30"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(select_sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)
# select_products_by_price(db_name)

def found_product(db_file):
    found_sql = ("SELECT * FROM products WHERE product_title LIKE 'PS%'")
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(found_sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

# found_product(db_name)