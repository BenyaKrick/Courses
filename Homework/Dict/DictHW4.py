"""
4] Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.
 Результаты выведите на экран.
"""
_list1 = [i for i in range(5)]
_list2 = ["a", "b", "c", "d", "f"]
_dictonary = dict(zip(_list1, _list2))
print(_dictonary)