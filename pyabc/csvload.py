import csv
import psycopg2

from pyabc.config import *

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

# Вытащить первую строку
current = next(reader)
current
current[:-1]

fnew = open('obec_0.sql', 'w', encoding='utf-8')
fnew.write("create table ah_csv (\n")
for s in current[:-1]:
    fnew.write("    {0:10} {1},\n".format(s, 'varchar'))
fnew.write("    {0:10} {1}\n".format(current[-1:][0], 'varchar'))
fnew.write(");\n")
fnew.close()

# insert_data_query = "INSERT INTO cats (name, vek, color) VALUES (%s, %s, %s)"
s_cols = ", ".join(current)
s_cols
v_cols = "%s, " * (len(current)-1) +  "%s"
v_cols
insert_data_query = "INSERT INTO ah_csv ({}) VALUES ({})".format(s_cols, v_cols)
insert_data_query

db_params
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

for row in reader:
    dt = tuple(row)
    cursor.execute(insert_data_query, dt)

conn.commit()

if conn:
    cursor.close()
    conn.close()

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

