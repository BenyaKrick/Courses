_dict = {
    'Космополитен': 1, 'Мохито': 2, 'Май Тай': 3,
    'Мятный джулеп': 5, 'Кайпиринья': 6, 'Маргарита': 7,
    'Пина Колада': 8, 'Калифорния': 9, 'Лонг-Айленд Айс Ти': 10,
    'Яблочный мартини': 11, 'Кровавая Мэри': 12, 'Отвертка': 13,
    'Мартини Драй': 14, 'Дайкири': 15, 'Текила Санрайз': 16
}
price = int(input('Введите пожалуйста цену коктейля: '))

new_dict = {key: value for key, value in _dict.items() if value < price}
print('Коктейли по цене ниже', price, ':')
print(*new_dict.keys(), sep=', ')
