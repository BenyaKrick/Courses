from sql_hw2 import create_table
from sql_hw2 import create_connection

create_connection("server.db")


def main():
    return create_connection("server.db"), create_table("students")



if __name__ == '__main__':
    main()
