from mysql import connector

def connection(db_name):
    mydb = connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = f"{db_name}"
    )

    return mydb

def create_db(db_name):
    mydb = connection(db_name)    
    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE DATABASE {db_name}")
    print(f"Database named '{db_name}' was successfully created!")

if __name__ == "__main__":
    create_db("testecombinacao")
