# Пользователь вводит число. Необходимо вычислить его факториал. Результаты
# вывести на экран.
# Математические подсказки: Формулу можно представить в таком виде:
# n! = 1 * … * (n-2) * (n-1) * n.

symbol = list(i for i in input())
sum = 1
for i in symbol:
    sum *= int(i)
print(sum)
