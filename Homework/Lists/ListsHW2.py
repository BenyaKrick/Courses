"""[2] Пользователь вводит две строки. Необходимо определить, являются ли две строки анаграммами.
Анаграмма — это слова состоящие из одних и тех же букв, расположенных в разном порядке.
"""

string0, string1 = (input(f'Введите {i}ю строку: ') for i in range(1, 3))
count = 0  # задаем счетчик
if len(string0) != len(string1):  # сравниваем длину строк
    print('Строки не являются аннаграммами')
else:
    if sorted(string0.lower()) == sorted(string1.lower()):  # сравниваем отсортированные строки
        print('Строки являются аннаграммами')
    else:
        print('Строки не являются аннаграммами')
