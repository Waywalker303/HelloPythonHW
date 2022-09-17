# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
from typing import List

ListRandom = []
for i in range(10):
    ListRandom.append(randint(10, 21))
print(f'Начальный {ListRandom}')
print(f'Сумма чисел списка: {ListRandom[1::2]} равна: {sum(ListRandom[1::2])}\n')