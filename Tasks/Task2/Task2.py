"""
2. Необходимо написать программу, которая рандомно генерирует список целых чисел. После этого над
полученным списком необходимо осуществить действия, в результате которых будет получен кортеж
уникальных элементов списка в обратном порядке.
"""


from random import randint


_list = [randint(0, 99) for i in range(9)]
_list1 = sorted(set(_list), reverse=True)
print(tuple(_list1))