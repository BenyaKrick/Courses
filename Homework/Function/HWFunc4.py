"""
[4] Имеется список с произвольными данными. Необходимо преобразовать его в множество. Если какие-то элементы
нельзя хешировать, то пропускаем их.  Результаты выведите на экран. Использовать lambda-функции.
"""


from collections.abc import Hashable


def list_to_set(_list):
    _set = filter(lambda x: isinstance(x, Hashable), _string)

    return set(_set)


_string = 1, [2, 4, 6], 55, 55, {1, 2, 3}, (2, 2), 5.11, None, True
print(list_to_set(_string))
