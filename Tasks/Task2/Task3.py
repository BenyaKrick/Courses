from random import randint
try:
    _list = [randint(0, 9) for i in range(1, 10)]

    _dict = {i: _list.count(i) for i in _list}
    print(_dict)
    sorted_values = sorted(_dict.values(), reverse=True)
    _sorted = {}

    for i in sorted_values:
        for k in _dict.keys():
            if _dict[k] == i and len(_sorted) < 3:
                _sorted[k] = _dict[k]
    print(_sorted)
except Exception as e:
    print("Ошибка: ", e)