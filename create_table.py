from mysql import connector

def connection(db_name):
    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = f"{db_name}"
    )

    return mydb

def create_table(db_name, table_name):
    mydb = connection(db_name)    
    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, valores VARCHAR(5), soma INT(2))")
    print(f"Table named '{table_name}' was successfully created!")

if __name__ == "__main__":
    create_table("testecombinacao", "numeros")
