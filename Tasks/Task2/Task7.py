
_set = {1, 2, 3, 4, 5, 17}
_set1 = {1, 5, 7, 8, 9, 11}
_set2 = {1, 2, 3, 8, 0, 76}
try:
    how = input('Выполнить симметричную разность ("Yes"/"NO"): ')
    if how.lower() == "yes":
        print(f'Результат симметричной разница = {_set^_set1^_set2}')
    else:
        print(f'Резльтат разницы = {_set - _set1 - _set2}')
except Exception as e:
    print("Ошибка: ", e)
