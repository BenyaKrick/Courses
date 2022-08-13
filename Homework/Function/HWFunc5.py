"""
[5] Написать функцию-декоратор, которая вычисляет время выполнения декорируемой функции,
а также выводит на экран имя функции и ее параметры.
"""
from datetime import datetime
import time
def data_time(func):
    start_time = datetime.now()
    time.sleep(5)

    return (datetime.now() - start_time)
@data_time
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))
print(sum_range(4, 1))
