import csv
import psycopg2

from pyabc.config import *

# Интерполяция строк
t1 = 'T1'
s1 = 'S1'
v1 = 'V1'
"INSERT INTO {0} ({0}) VALUES ({0}, {2} ..:.. {1})".format(t1, s1, v1)
f"INSERT INTO {t1} ({t1}) VALUES ({t1}, {v1} ..:.. {s1})"


# "\n"
f = open('.\\ah_csv\obec_0.csv', 'r', encoding='windows-1250')
#csv.register_dialect('excel-semicolon', delimiter=';')
# Автоматически определить диалект на базе первых 100 символов
dialect = csv.Sniffer().sniff(f.read(100))
f.seek(0)
# Можно посмотреть особенности диалекта, например
# Разделитель - delimeter
dialect.delimiter
# ';'
dialect.doublequote
dialect.escapechar
dialect.lineterminator
# '\r\n'
dialect.quotechar
# '"'
#reader = csv.reader(f, dialect='excel-semicolon')
reader = csv.reader(f, dialect = dialect)


##############################
#       Начало функций
##############################

def open_csv(filename):
    f = open(filename, 'r', encoding='windows-1250')
    # Автоматически определить диалект на базе первых 100 символов
    dialect = csv.Sniffer().sniff(f.read(50))
    f.seek(0)
    return csv.reader(f, dialect = dialect)

# Файл-скрипт для создания таблицы
def sql_create_tbl(filename, tablename, cols):
    fnew = open(filename, 'w', encoding='utf-8')
    fnew.write("create table {} (\n".format(tablename))
    for s in cols[:-1]:
        fnew.write("    {0:10} {1},\n".format(s, 'varchar'))
    fnew.write("    {0:10} {1}\n".format(cols[-1:][0], 'varchar'))
    fnew.write(");\n")
    fnew.close()

# Строка-скрипт для создания таблицы
def query_create_tbl(tablename, cols):
    query = []
    query.append("create table {} (\n".format(tablename))
    for s in cols[:-1]:
        query.append("    {0:10} {1},\n".format(s, 'varchar'))
    query.append("    {0:10} {1}\n".format(cols[-1:][0], 'varchar'))
    query.append(");\n")
    return "".join(query)

# Создание строки запроса на вставку в таблицу
def gen_insert(tablename, col_list):
    # Образец "INSERT INTO table_name (name, vek, color) VALUES (%s, %s, %s)"
    s_cols = ", ".join(col_list)
    v_cols = "%s, " * (len(col_list)-1) +  "%s"
    return "INSERT INTO {} ({}) VALUES ({})".format(tablename, s_cols, v_cols)

# Сохранение таблицы в БД
def save_table(db_params, insert_query, reader):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        for row in reader:
            dt = tuple(row)
            cursor.execute(insert_query, dt)

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
        # Идентичная команда
        # print("Ошибка: {}".format(error))
    finally:
        if conn:
            cursor.close()
            conn.close()

# Выполнение запроса в БД, например для создания таблицы
def exec_query(db_params, query):
    try:
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()

def create_load_tbl(db_params, csv_file):
    reader = open_csv(f'.\\ah_csv\{csv_file}.csv')
    col_names = next(reader)
    create_query = query_create_tbl(csv_file, col_names)
    exec_query(db_params, create_query)
    insert_query = gen_insert(csv_file, col_names)
    save_table(db_params, insert_query, reader)


# Открыть файл
reader = open_csv('.\\ah_csv\obec_0.csv')

# Прочитать первую строку
col_names = next(reader)

# Создать sql скрипт
sql_create_tbl('ah_0.sql', 'ah_csv', col_names)

insert_query = gen_insert('ah_csv', col_names)
save_table(db_params, insert_query, reader)


csv_load_list = [
    'kraj_0',
    'ku_0',
    'obec_0',
    'okres_0',
    'sr_0'
]

for item in csv_load_list:
    create_load_tbl(db_params, item)

create_load_tbl(db_params, 'kraj_0')
create_load_tbl(db_params, 'ku_0')
create_load_tbl(db_params, 'obec_0')
create_load_tbl(db_params, 'okres_0')
create_load_tbl(db_params, 'sr_0')

# Пример удаления таблицы - Выволнение SQL команды 'DROP TABLE SR_0'
# exec_query(db_params, 'DROP TABLE SR_0')

# res1 = func1()
# res2 = func2()
# res3 = func3(res1)

f.close()

# SELECT * FROM TBNAME WHERE a>10;

# CURSOR>   STR1 DATA1, DATA2
#           STR2 DATA1, DATA2
#           STR3 DATA1, DATA2
#           ... 
#           STRN DATA1, DATA2

