"""
[1] Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd': 600}.
Объедините их в один при помощи встроенных функций языка Python. Результаты выведите на экран.
"""
dictionary_1 = {'a': 300, 'b': 400}.update({'c': 500, 'd': 600})
dictionary_1.update({'c': 500, 'd': 600})
print(dictionary_1)