"""[2] Пользователь вводит  строку и символ. Необходимо определить индексы первого и
последнего вхождения символа в строке, при этом нельзя использовать строковые методы для поиска.
"""
_string = input('Введите строку: ').lower()
letter = input('Введите символ: ').lower()
num = 0
counter = 0
while True:
    if _string[counter] == letter:
        num = counter
        break
    counter += 1
print(f'первое вхождение по индексу: {num}')

num = 0
counter = 0

while True:
    if _string[counter] == letter:
        num = counter
        break
    counter -= 1
print(f'последнее вхождение по индексу: {num}')
