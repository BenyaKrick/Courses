"""[3] Дан кортеж с температурой за несколько дней (каждый элемент – средняя температура за день).
Посчитать среднюю температуру в течении всех дней. Результаты вывести на экран."""

_tuple = (23, 43, 65, 11, 87, 34)
print(f'Средняя температура за {len(_tuple)} равна {sum(_tuple)//len(_tuple)}')