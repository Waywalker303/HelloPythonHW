# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

userText = int(input('Введите число: ')) 

def numbers(userText):
    summ = 0
    for i in range(userText):
        number = int(input(f'Введи число {i + 1} '))
        number = (1+1/number)**number
        summ = number + summ
        i += 1
    return summ

print('Сумма чисел равна',round((numbers(userText)), 2))
