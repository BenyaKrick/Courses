"""
[1] Создайте таблицу учеников (ФИО + номер группы). Заполните таблицу 10-ю записями. Выберите записи только
с четными id.
[2] Измените таблицу учеников, добавив поле email. Обновите таблицу, заполнив поле email. Напишите запрос
для нахождения дублей в поле email.
"""
import psycopg2
from SQLConfig import host, user, password, name, port


def create_connect(db_name, db_user, db_password, db_host, db_port):
    con = None
    try:
        con = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Соединение установлено")
    except Exception as e:
        print(f'Ошибка: "{e}"')
    return con


def create_table(con):
    cur = con.cursor()
    cur.execute('''CREATE TABLE students
         (id serial PRIMARY KEY,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         middle_name TEXT NOT NULL,
         group_number TEXT NULL);''')
    print("Таблица создана")
    con.commit()


def add_Email():
    cur = con.cursor()
    cur.execute('''ALTER TABLE students ADD email VARCHAR(30);''')

    print('Столбец добавлен')
    con.commit()


def main():
    cur = con.cursor()
    cur.execute(
        """INSERT INTO students (first_name, last_name, middle_name, group_number) VALUES
        ('dfdffdg', '1sdfdfd', 'ejh', 1),
        ('nnkljk', 'nnlk', 'uioiuo', 3),
        ('kll', 'vjbkk', 'jnkn', 2),
        ('fhfdhg', 'fgfg', 'fghg', 2),
        ('hjb', 'gjhk', 'jkl', 2),
        ('jknnl', 'jkk', 'ujk', 4),
        ('jkl', 'bjk', 'njkkn', 4),
        ('nnkljk', 'nnlk', 'uioiuo', 3),
        ('kll', 'vjbkk', 'jnkn', 2),
        ('fgf', 'fgf', 'gdfgdf', 5);"""
    )

    cur.execute('''UPDATE students SET email = 'fdgd2@DFGF.ru';''')
                
    print("Данные записаны")
    cur.execute('SELECT * from students WHERE id % 2 = 0;')
    cur.execute("""SELECT * FROM Students WHERE email IN (SELECT email FROM Students GROUP BY email
    HAVING count(*)>1);""")
    con.commit()
    con.close()


con = create_connect(name, user, password, host, port)
cur = create_table(con)
add_Email()

if __name__ == "__main__":
    main()
