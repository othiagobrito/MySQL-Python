def select_single_info():

    from mysql import connector
    from random import randint

    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "testecombinacao"
    )

    mycursor = mydb.cursor()

    id_number = randint(1, 4)
    mycursor.execute(f"SELECT * FROM numeros WHERE id='{id_number}'")

    myresult = mycursor.fetchall()

    for id, combination, sum_ in myresult:
        return(f"ID: {id} - Combination: {combination} - Sum {sum_}")

if __name__ == "__main__":
    print(select_single_info())
