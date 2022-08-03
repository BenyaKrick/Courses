from random import randint

_list = [randint(0, 9) for i in range(0, 10)]
print(_list)

try:
    num = int(input('Введите делимое: '))
    for i in _list:
        result = num / i
        print(result)
except Exception as e:
    print("Ошибка: ", e)
