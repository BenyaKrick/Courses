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

        print(f'количество латинских букв = {_count1}, Cтрок в тексте = {_count+1}')

except Exception as e:
    print("Ошибка при работе с файлом:", e)
