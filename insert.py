from mysql import connector
from itertools import combinations

def connection(db_name):
    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = f"{db_name}"
    )

    return mydb

def insert(db_name, table_name):
    mydb = connection(db_name)    
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
        sql = f"INSERT INTO {table_name} (valores, soma) VALUES ('{f_value}', {s})"
        mycursor.execute(sql)
        mydb.commit()

if __name__ == "__main__":
    insert("testecombinacao", "numeros")
