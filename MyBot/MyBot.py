import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("TofuBot-Mariane")

def assign_move(square):
    directions = {NORTH, WEST, SOUTH, EAST}
    areAllNeighborsMe = True
    neighbors = enumerate(game_map.neighbors(square))
    numbOfNeighbors = 0

    for direction, neighbor in neighbors:
        directions.remove(direction)
        numbOfNeighbors += 1
        if neighbor.owner != myID:
            areAllNeighborsMe = False
            #capture du voisin s'il est plus faible que nous
            if neighbor.strength < square.strength:
                return Move(square, direction)
    
    #pièce centrale - on tente de mettre la force sur les cotes
    if areAllNeighborsMe and numbOfNeighbors == 4 and square.strength > 0:
        return Move(square, random.choice((NORTH, SOUTH, EAST, WEST)))
    #si notre piece n'est assez forte on reste
    if square.strength < min(2 * square.production,128) or len(directions) == 0:
        return Move(square, STILL)
    #si notre piece est assez forte on la bouge dans les directions qui ne sont pas encore prises
    else:
        return Move(square, random.choice(tuple(directions)))


while True:
    game_map.get_frame()
    # target = game_map.get_direction_toward_with_A_star(square, game_map.contents[0][0])
    # donne le direction pour aller vers la case 0 a partir du carre donne
    # moves = [Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))) for square in game_map if square.owner == myID]
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)