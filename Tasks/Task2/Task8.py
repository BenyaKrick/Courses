from random import randint

try:
    _list = set([randint(0, 9999) for i in range(1, 10000)])
    _list1 = set([randint(0, 9999) for i in range(1, 10000)])
    _listresult = list(_list & _list1)

    print(_listresult)
except Exception as e:
    print("Ошибка: ", e)
