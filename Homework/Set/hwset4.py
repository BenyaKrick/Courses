"""
[4] Предоставлен список натуральных чисел. Требуется сформировать из них множество.
Если какое-либо число повторяется, то преобразовать его в строку по образцу:
например, если число 4 повторяется 3 раза, то в множестве будет следующая запись:
само число 4, строка «44» (второе повторение, т.е. число дублируется в строке),
строка «444» (третье повторение, т.е. строка множится на 3).  Результаты выведите на экран.
"""
from random import randint


in_list = [randint(0, 10) for _ in range(10)]
print(in_list)

result_set = set()
for index, item in enumerate(in_list):
    count = in_list[:index + 1].count(item)
    new_item = item if count == 1 else str(item) * count
    result_set.add(new_item)

print(result_set)
