"""
[1] Имеется список с произвольными данными. Необходимо преобразовать его в множество.
Если какие-то элементы нельзя хешировать, то пропускаем их.  Результаты выведите на экран.
"""
from collections import Hashable
_list = [1, 2, 3, 4, 5, 6, ['q', 'w', 'e'], ('v', True, False)]
_set = set(item for item in _list if isinstance(item, Hashable))
print(_set)
