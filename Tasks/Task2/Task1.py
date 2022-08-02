try:
    _tuple = sorted(tuple((i for i in range(50) if type(i) != float)))
    print(tuple(_tuple))
except Exception as e:
    print("Ошибка: ", e)
