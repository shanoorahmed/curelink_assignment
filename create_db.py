import sqlite3

def create_table():
    try:
        sqliteConnection = sqlite3.connect('data.db')
        sqlite_create_table_query_1 = '''CREATE TABLE User (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE);'''
        sqlite_create_table_query_2 = '''CREATE TABLE Newsletter (
                                    id INTEGER PRIMARY KEY,
                                    topic TEXT NOT NULL,
                                    message text NOT NULL);'''
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query_1)
        cursor.execute(sqlite_create_table_query_2)
        sqliteConnection.commit()
        print("SQLite table created")
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

create_table()