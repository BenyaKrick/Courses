"""
4. Напишите программу, которая содержит генератор calculation(), который принимает два параметра и вычисляет сумму и
разность. Сперва возвращается сумма, потом разность. Результат вывести на экран.
"""


def calculation(a, b):
    amount = a + b
    yield amount
    diff = a - b
    yield diff


obj = calculation(2, 4)
print(next(obj))
print(next(obj))
