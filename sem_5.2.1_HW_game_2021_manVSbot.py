# **5.2.** 
# a) Добавьте игру против бота

def game2(sweets):
    user = False
    count = 1
    while sweets > 0:
        if user == True:
            game2_bot(sweets)
        if user == False:            
            user_request = int(input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        while user_request > 28:
            print(f'Игрок {int(user)+1} максимум 28!')
            user_request = int(
                input(f'Игрок {int(user)+1} введите количество конфет (от 1 до 28): '))
        sweets -= user_request
        print(f'осталось {sweets}')
        count += 1
        user = not(user)
        if sweets == 0:
            print(f'Игрок {int(user)+1} победил!')


def game2_bot(sweets):
    return (sweets % 29) - 1


game2(100) # количество конфет