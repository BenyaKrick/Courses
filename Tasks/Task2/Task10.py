"""
10. Имеется файл file.txt с текстом. Напишите программу, которая выводит следующую статистику по тексту:
● количество букв латинского алфавита;
● число строк.
"""
_count = 0 #счетчик строк
_count1 = 0 #счетчик латинских букв


with open('file.txt', 'r', encoding='utf-8') as text:
    _line = text.read()

    for i in _line:
        if i == '\n':
            _count += 1
        if i.lower().isalpha():
            _count1 += 1
    text.seek(0)

    print(f'Количество латинских букв = {_count1}, Cтрок в тексте = {_count+1}')

