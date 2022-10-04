# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
    
# еслиб не дробные .. 
userText = int((input('Введите число: ')))
print(sum(map(int,str(userText))))



# Было
# userText = (input('Введите число: '))

# sum = 0
# for i in userText:
#     if i != '-':
#         if i != '.':
#             if i != ',':
#                 sum += int(i)
# print(sum)



