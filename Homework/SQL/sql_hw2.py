import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
      Id_name integer PRIMARY KEY not null 
      sur_name TEXT not null, 
      student_name TEXT not null, 
      middle_name TEXT not null,
      group_number INTEGER not null,
      )""")
db.commit()


# if __name__ == '__main__':
#     pass
