# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
from typing import List

ListRandom = []
ListSumm = []
for i in range(6):
    ListRandom.append(randint(0, 10))

for i in range((len(ListRandom))//2):   
    ListSumm.append(ListRandom[i]*ListRandom[len(ListRandom)-1-i]) 
    
print(ListRandom)
print(ListSumm)


