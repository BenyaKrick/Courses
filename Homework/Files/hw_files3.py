"""
[3] Имеется файл file.txt с текстом на латинице. Напишите программу, которая выводит
следующую статистику по тексту:
- количество букв латинского алфавита;
- число слов;
- число строк.
"""
_count = 0 #счетчик строк
_count1 = 0 #счетчик латинских букв

try:
    with open('file.txt', 'r', encoding='utf-8') as text:
        _line = text.read()

        for i in _line:
            if i == '\n':
                _count += 1
            if 'a' <= i.lower() <= 'z':
                _count1 += 1
        text.seek(0)
        _line1 = text.read().split()

        print(f'количество латинских букв = {_count1}, число слов = {len(_line1)} Cтрок в тексте = {_count+1}')

except Exception as e:
    print("Ошибка при работе с файлом:", e)
