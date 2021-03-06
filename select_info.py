from mysql import connector

def connection(db_name):
    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = f"{db_name}"
    )

    return mydb

def select_info(db_name, table_name):
    mydb = connection(db_name)    
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM {table_name}")

    myresult = mycursor.fetchall()

    for id, combination, sum_ in myresult:
        print(f"ID: {id} - Combination: {combination} - Sum {sum_}")

if __name__ == "__main__":
    select_info("testecombinacao", "numeros")
