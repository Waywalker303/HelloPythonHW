# Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

userText = int(input('Введите число: '))
fac = lambda a, b:  a * b
faktorial = 1
for i in range(userText):
    i +=1
    faktorial = fac(faktorial,i)
    print(faktorial, end=' ')
print('\n')    


# было
# userText = int(input('Введите число: '))

# faktorial = 1
# list = [1,]
# while userText > 1:
#     faktorial *= userText
#     userText -= 1
#     list.append(faktorial)
    
# print(list)    