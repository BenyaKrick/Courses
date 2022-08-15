"""
[6] Напишите генератор custom_ange(start, end, step), который генерирует все целые числа от значения
«start» до величины «end» включительно с шагом «step». Если пользователь задаст первое число большее
чем второе, просто поменяйте их местами. «step» по умолчанию равен = 1. Также не допускать ввод дробных чисел.
"""


def custom_ange(start, end, step=1):
    if start > end:
        start, end = end, start
    try:
        return (_ for _ in range(start, end + 1, step))
    except ValueError:
        print("Ошибка ввода, допускаются только целые числа")


print(custom_ange(0, 'r'))
