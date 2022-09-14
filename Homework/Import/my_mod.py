"""
1. Основы операций импортирования. Напишите программу, которая подсчитывает строки и символы в файле. Создайте модуль
Python по имени my_mod.py, который экспортирует три имени верхнего уровня.
   о Функция count_lines(name) читает входной файл и подсчитывает количество строк в нем (подсказка: file.readlines
   выполняет большую часть работы, a len делает остаток, хотя вы могли бы подсчитывать посредством for и файловых
   итераторов, чтобы поддерживать также крупные файлы).
   о Функция count_chars(name) читает входной файл и подсчитывает количество символов в нем (подсказка: file.read
   возвращает одиночную строку, которую можно использовать аналогичными способами).
   о Функция test(name) вызывает обе функции подсчета с заданным именем входного файла.
Все три функции модуля my_mod должны ожидать передачи строки с именем файла.
2. __main__. Добавьте в модуль my_mod строку, которая вызывает функцию test автоматически, когда модуль запускается как
 сценарий, но не в случае его импортирования. По всей видимости, в добавленной строке вы будете проверять значение
 __ name__ на предмет равенства строке "__ main__".
3. Вложенные операции импортирования. Создайте второй модуль, my_client.py, который импортирует модуль my_mod и
тестирует его функции.
4. Операции импортирования пакетов. Импортируйте свой файл из пакета. Создайте подкаталог по имени my_pkg внутри
рабочего каталога, переместите в новый подкаталог файл модуля my_mod.py, созданный в упражнении 1, и попробуйте
импортировать его с помощью операции импортирования пакета в форме import mypkg.mymod, после чего вызовите функции
модуля. Попробуйте извлечь функции подсчета и посредством from тоже.
"""


def count_lines(name):
    _count = 0  # счетчик строк

    try:
        with open(name, 'r', encoding='utf-8') as text:
            _line = text.read()

            for i in _line:
                if i == '\n':
                    _count += 1
            text.seek(0)
            _line1 = text.read().split()

    except Exception as e:
        print("Ошибка при работе с файлом:", e)
    return _count + 1


def count_chars(name):
    _count1 = 0  # счетчик букв
    try:
        with open(name, 'r', encoding='utf-8') as text:
            _line = text.read()
            _count1 = len(_line)

    except Exception as e:
        print("Ошибка при работе с файлом:", e)
    return _count1


def test(name):
    return count_lines(name), count_chars(name)

if __name__ == "__main__":
    test('file.txt')