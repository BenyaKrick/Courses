# Дана строка, содержащая натуральные числа и слова. Необходимо сформировать
# список из чисел, содержащихся в этой строке. Результаты вывести на экран.
# Например, задана строка "abc83 cde7 1 b 24". На выходе мы должны получить
# список [83, 7, 1, 24].

symbol = input()
_list = []

num = ''
for i in symbol:
    if i.isdigit():
        num += i
    else:
        if num != '':
            _list.append(int(num))
            num = ''
if num != '':
    _list.append(int(num))

print(_list)
