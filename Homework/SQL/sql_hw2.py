import sqlite3
from sqlite3 import Error


def create_connection(db_server):
    conn = None
    try:
        conn = sqlite3.connect(db_server)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


db= create_connection('server.db')
create_table(db, 'students')
if __name__ == '__main__':
    create_connection()
