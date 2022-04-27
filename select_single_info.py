from mysql import connector
from random import randint

def connection(db_name):
    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = f"{db_name}"
    )

    return mydb

def select_single_info(db_name, table_name, id):
    mydb = connection(db_name)    
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM {table_name} WHERE id='{id}'")

    myresult = mycursor.fetchall()

    for id, combination, sum_ in myresult:
        print(f"ID: {id} - Combination: {combination} - Sum {sum_}")

if __name__ == "__main__":
    select_single_info("testecombinacao", "numeros", randint(1,4))
