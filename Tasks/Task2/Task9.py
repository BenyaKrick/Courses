from random import randint

_list = [randint(0, 9) for i in range(0, 10)]

try:
    num = float(input('Введите делимое: '))
    for i in _list:
        result = num / i
except ZeroDivisionError:
    print("Деление на ноль ")

except Exception as e:
    print("Введено не числовое значение: ", e)
