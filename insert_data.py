import sqlite3

def insert_data_into_User(name, email):
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO User (name, email) 
                            VALUES (?, ?)"""

        cursor.execute(sqlite_insert_query,(name,email))
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def insert_data_into_Newsletter(topic, message):
    try:
        sqliteConnection = sqlite3.connect('data.db')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO Newsletter (topic, message) 
                            VALUES (?, ?)"""

        cursor.execute(sqlite_insert_query,(topic,message))
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

flag = True
while flag:
    print("Enter 1 to insert into User")
    print("Enter 2 to insert into Newsletter")
    print("Enter 0 to quit")
    num = input()
    if num == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        insert_data_into_User(name, email)
    elif num == '2':
        topic = input("Enter topic: ")
        message = input("Enter message: ")
        insert_data_into_Newsletter(topic, message)
    else :
        flag = False

    if(flag == False):
        break
