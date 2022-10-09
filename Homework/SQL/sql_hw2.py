import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS students (
      Id_name INTEGER not null, 
      sur_name TEXT not null, 
      student_name TEXT not null, 
      middle_name TEXT not null,
      age INTEGER not null,
      student_email not null
      )""")
db.commit()

sur_name = input('enter surname: ')
student_name = input('enter name: ')
middle_name = input('enter middlename: ')
age = int(input('enter age : '))
student_email = input('enter email: ')

sql.execute("SELECT * FROM students")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO students VALUES ('{0}', {sur_name}', '{student_name}', '{middle_name}', '{0}', "
                f"'{student_email}')")
    db.commit()
else:
    print("this students is here")
for value in sql.execute("SELECT * FROM students"):
    print(value)

# if __name__ == '__main__':
#     pass
