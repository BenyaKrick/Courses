from random import randint
_list = [randint(0, 9) for i in range(9)]
print(tuple(list(set(_list))[::-1]))
