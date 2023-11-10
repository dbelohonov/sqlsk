import csv
# "\n"
f = open('.\\ah_csv\obec_0.csv', encoding='windows-1250')
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

for row in reader:
    print(row)



# res1 = func1()
# res2 = func2()
# res3 = func3(res1)

