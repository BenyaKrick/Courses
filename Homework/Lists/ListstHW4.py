"""Пользователь вводит  строку и символ. Необходимо определить индексы первого и последнего вхождения символа в строке.
"""
string = input('Введите строку: ')
letter = input('Введите символ: ')
if letter not in string:
    print('Такого символа нет в строке!')
else:
    print(f'Первое вхождение: {string.find(letter)}\nПоследнее вхождение: {string.rfind(letter)}')
