"""Пользователь вводит строку и символ. Определить количество вхождений символа в строку,
независимо от регистра.
"""
string = input('Введите строку: ')
letter = input('Введите символ: ')
string, letter = string.lower(), letter.lower()

print(string.count(letter))
