import sqlite3
from itertools import product

hw_9 = "Homework_9.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

create_connection(hw_9)


def print_stores(db_file):
    get_sql = "SELECT store_id, title FROM stores"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(get_sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)

def get_products_by_store(db_file, store_id):
    get_product = """
    SELECT p.title, c.title, p.unit_price, p.stock_quantity
    FROM products as p
    JOIN categories c ON p.category_code = c.code
    WHERE p.store_id = ?
    """
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(get_product, (store_id,))
            products = cursor.fetchall()
            if products:
                for product in products:
                    print(f"\nНазвание продукта: {product[0]}")
                    print(f"Категория: {product[1]}")
                    print(f"Цена: {product[2]}")
                    print(f"Количество на складе: {product[3]}")
            else:
                print("\nВ выбранном магазине нет продуктов.")
    except sqlite3.Error as error:
        print(f"Ошибка базы данных: {error}")
        return


while True:
    print_stores(hw_9)
    id_citi = input("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    if id_citi == '0':
        print("Программа завершилась! ")
        break
    else:
        get_products_by_store(hw_9, int(id_citi))