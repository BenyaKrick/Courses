"""Вычислить остаток от деления и целую часть, не используя знаки % и //"""
from decimal import Decimal #вызов модуля
from colorama import Fore #так симпотичней будет

delim, delit = [float(i) for i in input('Введите делимое и делитель: ').split()] #ввод данных, исключая str

while True: #исключение деления на ноль
    if delit == 0:
        print("Деление на '0'!")
        delit = float(input('Повторите ввод делителя: '))
    else:
        break

result = Decimal(delim) / Decimal(delit) #теперь я стал чуточку умнее

if delit > 0 and delim > 0 or delit < 0 and delim < 0:
    print(Fore.MAGENTA + f'Целая часть равна: {(int(result))}')
    print(Fore.CYAN + f'Остаток равен: {(Decimal(delim) - Decimal(int(result)) * Decimal(delit))}')
else:
    print(Fore.MAGENTA + f'Целая часть равна: {(round(result))}')
    print(Fore.CYAN + f'Остаток равен: {(Decimal(delim) - Decimal(round(result)) * Decimal(delit))}')
#thanks for the very interesting homework