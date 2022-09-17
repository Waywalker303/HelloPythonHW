# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
list = []

for i in range(-n,n+1):
    list.append(i)
print(list)

res = 1
with open('sem_2.4_HW_number.txt','w') as data:
    data.write('4 \n')
    data.write('2 \n')
    data.write('3 \n')
    data.write('1 \n')
    data.write('2 \n')

patch = 'sem_2.4_HW_number.txt'
data = open(patch, 'r')


userElementOne = int(input('Введите позицию элимента 1: '))
userElementTwo = int(input('Введите позицию элимента 2: '))

print (f'{(list[userElementOne]-1)} + {(list[userElementTwo]-1)} = {(list[userElementOne]-1)+(list[userElementTwo]-1)}')