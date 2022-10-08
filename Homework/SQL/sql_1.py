import sqlite3
from sqlite3 import Error


class Students:
    def __init__(self, name, subname, middlename, age, mail):
        self.name = name
        self.subname = subname
        self.middlename = middlename
        self.age = age
        self.mail = mail

    def set_students(self, name, subname, middlename, age, mail):
        self.name = name
        self.subname = subname
        self.middlename = middlename
        self.age = age
        self.mail = mail
        return name, subname, middlename, age, mail

stude = Students('sergei', 'vit', 'baronin', '44', "srt@yandex.ru")
# stude1 = Students('1', '2', '3', '4')
# stude2 = Students('a', 'b', 'c', 'd')
# stude3 = Students('e', 'f', 'g', 'h')
# stude4 = Students('w', 'n', 'k', 'z')
# stude5 = Students('b', 'm', 'l', 'r')
# stude6 = Students('1', '2', '3', '11')
# stude7 = Students('12', '22', '23', '24')
# stude8 = Students('31', '32', '33', '34')
# stude9 = Students('41', '42', '43', '44')
print(stude.__dict__)
# print(stude1.__dict__)
# print(stude2.__dict__)
# print(stude3.__dict__)
# print(stude4.__dict__)
# print(stude5.__dict__)
# print(stude6.__dict__)
# print(stude7.__dict__)
# print(stude8.__dict__)
# print(stude9.__dict__)

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
