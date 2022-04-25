from mysql import connector

mydb = connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testecombinacao"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM numeros")

myresult = mycursor.fetchall()

for id, combination, sum_ in myresult:
    print(f"ID: {id} - Combination: {combination} - Sum {sum_}")
