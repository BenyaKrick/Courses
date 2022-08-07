"""
[4] Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран
содержимое этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству
букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы
они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл
 forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть
 заменены на ****.
"""
string = input('введите название файла для поиска : ')

try:
    import os
    _list = os.listdir()
    print(_list)
    for i in _list:
        if i == string:
            with open(i, 'r', encoding='utf-8') as file:
                searchfile = file.read()
                for j in searchfile:
                    if j == 'exam':
                        searchfile[j] = '****'
        print(searchfile)


    with open(i, 'w', encoding='utf-8') as file:
        searchfile = file.write(searchfile)
        print(searchfile)

except Exception as e:
    print("Ошибка при работе с файлом:", e)