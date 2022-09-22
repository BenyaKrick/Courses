"""
Напишите программу, которая бы «Подбрасывала» условную монету 100 раз и
сообщала, сколько раз выпал орел, а сколько - решка.
"""
import random

eagle = 0
tail = 0
_count = 0
while _count != 100:
    coin = random.randint(0, 1)
    _count += 1
    if coin == 0:
        eagle += 1

    elif coin == 1:
        tail += 1

print("Орел выпал", eagle)
print("Решка выпала", tail)
