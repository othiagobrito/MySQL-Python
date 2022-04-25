import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testecombinacao"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testeCombinacao")
mycursor.execute("CREATE TABLE numeros (id INT AUTO_INCREMENT PRIMARY KEY, valores VARCHAR(5), soma INT(2))")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("DESCRIBE numeros")

for i in mycursor:
    print(i)
