# Создайте программу для игры в ""Крестики-нолики"".


maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# победные комбинации
wins = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]
 

def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8]) 
    
   

def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
    

def get_result():
    win = ""
 
    for i in wins:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
             
    return win


game_over = False
gamer1 = True
 
while game_over == False:
 

    print_maps()
 

    if gamer1 == True:
        symbol = "X"
        step = int(input("Ходит игрок 1: "))
    else:
        symbol = "O"
        step = int(input("Ходит игрок 2: "))
 
    step_maps(step,symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
 
    gamer1 = not(gamer1)        
 
      
print_maps()
print("Победил", win)     