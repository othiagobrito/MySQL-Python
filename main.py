import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testecombinacao"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
