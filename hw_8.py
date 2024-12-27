import sqlite3

hw_8 = "Homework_8.db"

# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except sqlite3.Error as e:
#         print(e)
#     return conn

# db_file1 = create_connection(hw_8)
# if db_file1 is not None:
#     print("Connection successful")

def print_cities(db_file):
    get_sql = "SELECT id, title FROM cities"
    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()
            cursor.execute(get_sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as error:
        print(error)

def get_students_by_city(db_file, city_id):
    get_students_sql = "SELECT first_name, last_name FROM students WHERE city_id = ?"
    get_country_sql = "SELECT title FROM countries WHERE id = (SELECT country_id FROM cities WHERE id = ?)"
    get_city_sql = "SELECT title, area FROM cities WHERE id = ?"

    try:
        with sqlite3.connect(db_file) as conn:
            cursor = conn.cursor()

            cursor.execute(get_students_sql, (city_id,))
            students = cursor.fetchall()

            cursor.execute(get_country_sql, (city_id,))
            country = cursor.fetchone()

            cursor.execute(get_city_sql, (city_id,))
            city = cursor.fetchone()
        if students:
            print(students)
            print(country)
            print(city)
            for student in students:
                print(f"\nУченики: {student[0]} {student[1]}, город: {city[0]}, площадь: {city[1]} км², страна: {country[0]}:")
        else:
            print("\nНет учеников в выбранном городе.")

    except sqlite3.Error as error:
        print(error)

while True:
    print_cities(hw_8)
    id_citi = input("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0: ")
    if id_citi == '0':
        print("Программа завершилась! ")
        break
    else:
        get_students_by_city(hw_8, int(id_citi))