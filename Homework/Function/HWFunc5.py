"""
[5] Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
а также выводит на экран имя функции и ее параметры.
"""


from datetime import datetime

time_now = datetime.now()


def decorating_func(own_func):
    def wrapper(*args, **kwargs):

        print(datetime.now() - time_now)
        return own_func(*args, **kwargs)

    return wrapper


@decorating_func
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


print(sum_range(1, 1000900))
