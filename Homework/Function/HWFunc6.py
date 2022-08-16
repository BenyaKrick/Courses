"""
[6] Напишите генератор custom_ange(start, end, step), который генерирует все целые числа от значения
«start» до величины «end» включительно с шагом «step». Если пользователь задаст первое число большее
чем второе, просто поменяйте их местами. «step» по умолчанию равен = 1. Также не допускать ввод дробных чисел.
"""


def custom_age(start, end, step=1):
    if start > end:
        start, end = end, start

    yield from range(start, end + 1, step)


num_fromgen = custom_age(1, 10, 4)
for index in num_fromgen:
    print(index)
