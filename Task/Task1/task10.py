# Пользователь вводит строку. В строке заменить пробелы звездочкой. Если
# встречается подряд несколько пробелов, то их следует заменить одним знаком
# "*", пробелы в начале и конце строки удалить. Результаты вывести на экран.

_string = input()
i = 0

while _string[i] == ' ':
    i += 1
s = _string[i:]

i = len(s)
while s[i - 1] == ' ':
    i -= 1
s = s[:i]

_string_new = s[0]
i = 1
while i < len(s):
    if s[i] != ' ':
        _string_new += s[i]
    elif s[i - 1] != ' ':
        _string_new += '*'
    i += 1
print(_string_new)
