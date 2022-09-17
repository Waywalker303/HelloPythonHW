# Реализуйте алгоритм перемешивания списка.

import random
listOld = [1, 2, 3, 4, 5]
print(listOld)

for i in range(len(listOld)):
    d = random.randint(0,(len(listOld)))
    listOld += [listOld.pop(random.randint(0,d))]
print(listOld)

# ? c вероятностью 1 к ~5 вылетает с ошибкой