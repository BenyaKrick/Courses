"""
Напишите проrрамму, которая бы считала по просьбе пользователя. Надо позволить пользователю ввести начало и конец счета,
а также интервал между называемыми целыми числами.
"""
start = int(input())
end = int(input())
sep = int(input())
for i in range(start, end, sep):
    print(i)