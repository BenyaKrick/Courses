"""
[2] Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
Результаты выведите на экран.
"""
dictionary_1 = {'a': 4, 'b': 4, 'c': 5}
result = 1
for i in dictionary_1:
    result *= dictionary_1.get(i)
print(result)
