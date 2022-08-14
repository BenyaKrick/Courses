"""
10. Имеется файл file.txt с текстом. Напишите программу, которая выводит следующую статистику по тексту:
● количество букв латинского алфавита;
● число строк.
"""
list_count = 0
alfa_count = 0


with open('file.txt', 'r', encoding='utf-8') as text:
    _line = text.read()

    for i in _line:
        if i == '\n':
            list_count += 1
        if i.lower().isalpha():
            alfa_count += 1

    print(f'Количество латинских букв = {alfa_count}, Cтрок в тексте = {list_count + 1}')
