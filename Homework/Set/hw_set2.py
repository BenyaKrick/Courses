"""
Дано 2 множества. Проанализировать их и вывести на экран  одного из сообщений
в зависимости от ситуации:
1 – «Объект {X2} является чистым супермножеством» (X2 < X1)
2 – «Объект {X1} является чистым супермножеством» (X1 < X2)
3 – «Множества равны» (==)
4 – «Супермножество не обнаружено»
"""
_set1 = {1, 2, 3, 4, 5, 6}
_set2 = {1, 2, 3, 4, 5}
if _set1 < _set2:
    print(f'«Объект {_set1} является чистым супермножеством»')
elif _set1 > _set2:
    print(f'«Объект {_set2} является чистым супермножеством»')
elif _set1 == _set2:
    print(f'«Множества равны»')
else:
    print('Супермножеств не обнаружено')
