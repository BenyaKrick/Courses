"""
Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите все числа, которые входят как в первый,
так и во второй список в порядке возрастания.
"""


from random import randint


_list = set([randint(0, 9999) for _ in range(1, 10000)])
_list1 = set([randint(0, 9999) for _ in range(1, 10000)])
_listresult = list(_list & _list1)

print(_listresult)
