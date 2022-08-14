"""
3. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в
качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество
этих чисел в имеющейся последовательности. На экран вывести словарь из 3-х самых часто встречаемых чисел.
"""


from random import randint


_list = [randint(0, 9) for i in range(1, 10)]
_dict = {i: _list.count(i) for i in _list}

print(_dict)
sorted_values = sorted(_dict.values(), reverse=True)
_sorted = {}

for i in sorted_values:
    for k in _dict.keys():
        if _dict[k] == i and len(_sorted) < 3:
            _sorted[k] = _dict[k]
    print(_sorted)
