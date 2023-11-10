import psycopg2

from pyabc.config import *

# SQL-запрос для выборки данных из таблицы
select_query = "SELECT * FROM cats"

try:
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Выполняем SQL-запрос
    cursor.execute(select_query)

    # Получаем имена колонок из cursor.description
    column_names = [desc[0] for desc in cursor.description]

    # Получаем результат запроса
    rows = cursor.fetchall()

    # Перебираем строки результата
    for row in rows:
        # Используем zip() для объединения имен колонок и значений
        row_data = dict(zip(column_names, row))
        print(row_data)

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Ошибка: {error}")
finally:
    if conn:
        cursor.close()
        conn.close()


# ----------------------------------------------------------------------------


# SQL-запрос для вставки данных
insert_data_query = "INSERT INTO cats (name, vek, color) VALUES (%s, %s, %s)"

data_to_insert1 = ('Clock', 3, 'black')
data_to_insert2 = ('Emma', 3, 'easy')
data_to_insert3 = ('White', 3, 'white')

data_list = [data_to_insert1, data_to_insert2, data_to_insert3]

try:
    # Устанавливаем соединение с базой данных
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Создаем таблицу
    # cursor.execute(create_table_query)
    # conn.commit()

    # Вставляем данные 1 строка
    # cursor.execute(insert_data_query, data_to_insert1)

    for dt in data_list:
        cursor.execute(insert_data_query, dt)
    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Ошибка: {error}")
finally:
    if conn:
        cursor.close()
        conn.close()

if conn:
    cursor.close()
    conn.close()


