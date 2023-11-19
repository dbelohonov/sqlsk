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

# Интерполяция строк
t1 = 'T1...'
s1 = 'S1.'
v1 = 'V1'
"INSERT INTO {0} ({0}) VALUES ({0}, {2} ..:.. {1})".format(2*2+5, t1 + s1, v1)
"INSERT INTO {param1} ({param1}) VALUES ({param2}, {param2} ..:.. {param3})".format(param1 = 2*2+5, param2 = t1 + s1, param3 = v1)
f"INSERT INTO {2+5+9} ({t1}) VALUES ({t1}, {v1} ..:.. {s1})"
print("+{:<20}+".format(t1))
print("+{:<20}+".format(s1))
print("+{:<20}+".format(v1))
print("+{:.^20b}+".format(25))

# Так делать нельзя
'abc' + 'cde' + 'dfg'

# Это правильный способ он не расходует оперативную память
slist = ['abc', 'cde', 'dfg']
"".join(slist)

tlist = ('abc', 'cde', 'dfg')
"".join(tlist)

di = {'a':'abc', 'b':'cde', 'c':'dfg'}
di.items()
"".join(di.keys())
di.values()
"".join(di.values())



