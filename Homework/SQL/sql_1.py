import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def main():
    database = r"students"

    sql_create_projects_table = """
    create table product 
    ( 
      key_id integer PRIMARY KEY not null, 
      sur_name TEXT not null, 
      student_name TEXT not null, 
      middle_name TEXT not null,
      age INTEGER not null,
      student_email not null
    );
    """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    create_connection(r"usersdb.db")
