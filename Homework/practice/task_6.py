'''
# Напишите цикл for, который выводит элементы
# словаря в отсортированном порядке (по возрастанию).
'''
_dic = {1: 6, 3: 4, 5: 2}
sorted_pairs = [(k, _dic[k]) for k in sorted(_dic.keys(), key=_dic.get, reverse=True)]
print(sorted_pairs)
