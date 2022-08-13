"""
[4] Имеется список с произвольными данными. Необходимо преобразовать его в множество. Если какие-то элементы
нельзя хешировать, то пропускаем их.  Результаты выведите на экран. Использовать lambda-функции.
"""
from collections.abc import Hashable


def list_to_set(_list):
    _set = set(map(lambda x: x, (i for i in _list if isinstance(i, Hashable))))
    return _set


_string = 1, [2], 55, 55, {1, 2, 3}, (2, 2), 5.11
print(list_to_set(_string))
