"""
[3] Напишите функцию, чтобы проверить, является ли строка панграммой или нет. Панграмма — фраза,
содержащая в себе все буквы алфавита.
"""


def text_pangrama(t):
    return not (set('abcdefghijklmnopqrstuvwxyz') - set(t.lower()))


text = input()

print(text_pangrama(text))
