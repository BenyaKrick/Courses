"""
[2] Напишите программу, которая принимает поисковый запрос и выводит названия текстовых файлов,
содержащих искомую подстроку. Все файлы располагаются в заданной директории.
"""
name = input('введите подстроку для поиска : ')
_count = 0
try:
    import os
    _list = os.listdir()


    for i in _list:
        with open(i, 'r', encoding='utf-8') as _file:
            _name =_file.read()
            if name in _name:
                print(f'название файла {i}')

except Exception as e:
    print("Ошибка при работе с файлом:", e)
