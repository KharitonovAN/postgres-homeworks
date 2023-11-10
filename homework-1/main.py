"""Скрипт для заполнения данными таблиц в БД Postgres."""
# Импорт функций:
import csv
import psycopg2

# Подключение к базам данных:
conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="1234"
)

# Создание курсора:
cur = conn.cursor()

with open('./north_data/employees_data.csv', 'r') as f:
    """Заполнение таблицы employees"""
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        employee_id, first_name, last_name, title, birth_date, notes = row
        cur.execute(
            "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
            "VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (employee_id) DO NOTHING",
            (employee_id, first_name, last_name, title, birth_date, notes)
        )


with open('./north_data/customers_data.csv', 'r') as f:
    """Заполнение таблицы customers"""
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        customer_id, company_name, contact_name = row
        cur.execute(
            "INSERT INTO customers (customer_id, company_name, contact_name) "
            "VALUES (%s, %s, %s) ON CONFLICT (customer_id) DO NOTHING",
            (customer_id, company_name, contact_name)
        )


with open('./north_data/orders_data.csv', 'r') as f:
    """Заполнение таблицы orders"""
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        order_id, customer_id, employee_id, order_date, ship_city = row
        cur.execute(
            "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) "
            "VALUES (%s, %s, %s, %s, %s) ON CONFLICT (order_id) DO NOTHING",
            (order_id, customer_id, employee_id, order_date, ship_city)
        )


conn.commit()
conn.close()
