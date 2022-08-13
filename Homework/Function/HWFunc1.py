"""
1] Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины
«end» включительно. Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
"""
def sum_range(start, end):
    sum = 0
    if end < start:
        star, end = end, start
    for i in range(start, end+1):
        sum += i
    return sum
print(sum_range(1, 4))
