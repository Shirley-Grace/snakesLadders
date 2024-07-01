import random


board_size = 100

# snakes and ladders
snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}

player_position = 0

while True:
    dice = random.randint(1, 6)
    
    player_position += dice
    
    if player_position in snakes:
        player_position = snakes[player_position]
    elif player_position in ladders:
        player_position = ladders[player_position]
    
    if player_position >= board_size:
        print("Congratulations, you won!")
        break
    

