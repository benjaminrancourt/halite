import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random
import math

myID, game_map = hlt.get_init()

# Hauteur de la carte
heigth = game_map.height

# Largeur de la carte
witdh = game_map.width

# Nombre de tours
numTurns = int(10 * math.sqrt(heigth * witdh))

# Tour courant
currentTurn = 0

# Points intercardinaux
interCardinalDirections = [
    (NORTH, EAST),
    (SOUTH, EAST),
    (SOUTH, WEST),
    (NORTH, WEST),
]

# Point intercardinal aléatoire
randomInterCardinalDirection = random.choice(interCardinalDirections)

hlt.send_init("TofuBot-Benjamin")

def assign_move(square):
    directions = {NORTH, WEST, SOUTH, EAST, STILL}
    areAllNeighborsMe = True
    neighbors = enumerate(game_map.neighbors(square))
    numbOfNeighbors = 0

    for direction, neighbor in neighbors:
        directions.remove(direction)
        numbOfNeighbors += 1

        if neighbor.owner != myID:
            areAllNeighborsMe = False

            # Capture du voisin s'il est plus faible que nous
            if neighbor.strength < square.strength:
                return Move(square, direction)
    
    # Pièce entourée de pièces amies
    if areAllNeighborsMe and numbOfNeighbors == 4:
        if square.strength < 32:
            return Move(square, STILL)

        return Move(square, random.choice(randomInterCardinalDirection))

    # Si notre piece n'est pas assez forte, on reste
    if square.strength < max(2 * square.production, 128) or len(directions) == 0:
        return Move(square, STILL)

    # Si notre piece est assez forte, on la bouge dans les directions qui ne sont pas encore prises
    return Move(square, random.choice(tuple(directions)))


while True:
    game_map.get_frame()
    # target = game_map.get_direction_toward_with_A_star(square, game_map.contents[0][0])
    # donne le direction pour aller vers la case 0 a partir du carre donne
    # moves = [Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))) for square in game_map if square.owner == myID]
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
    currentTurn += 1