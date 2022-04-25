import mysql.connector
from itertools import combinations

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testecombinacao"
)

mycursor = mydb.cursor()

numbers = list(range(1,5))
comb = []
for n in numbers:
    comb.append(str(n))

comb = combinations(comb, 3)
for i in comb:
    values = i
    f_value = ",".join(values)

    comb_numbers = []
    for c_n in i:
        comb_numbers.append(int(c_n))
    s = sum(comb_numbers)

    print(f"Combinação: {f_value} - Soma: {s}")
    sql = f"INSERT INTO numeros (valores, soma) VALUES ('{f_value}', {s})"
    mycursor.execute(sql)
    mydb.commit()
