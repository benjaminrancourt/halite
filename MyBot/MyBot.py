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

#choisir un milieu
middle = random.choice(tuple([square for square in game_map if square.owner == myID]))
directionsMatrix = [[-1 for x in range(heigth)] for y in range(witdh)]

hlt.send_init("TofuBot-Mariane")

def return_square(square):
    return square

def find_closest_square(square, list_squares):
    closest = square
    min_dist = float('inf')

    for sq in list_squares:
        dist = game_map.get_distance(square, sq) + 1000 * (sq.owner == 0)
        if dist < min_dist:
            min_dist = dist
            closest = sq
    
    return closest

def assign_move(square, enemiesSquares):
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

    #on trie les directions restantes selon leur force
    sortedDir = hlt.PriorityQueue()
    for direction in directions:
        sortedDir.put(direction, game_map.get_target(square, direction).strength)

    # Pièce entourée de pièces amies
    if areAllNeighborsMe and numbOfNeighbors == 4:
        if square.strength < 32:
            return Move(square, STILL)

        #sq1 = game_map.get_target(square, randomInterCardinalDirection[0])
        #sq2 = game_map.get_target(square, randomInterCardinalDirection[1])
        
        #if sq1.strength < sq2.strength:
        #    return Move(square, randomInterCardinalDirection[0])
        #else:
        #    return Move(square, randomInterCardinalDirection[1])

        #best_dir = directionsMatrix[square.x][square.y]
        #if best_dir != -1:
        #    return Move(square, best_dir)
        #else:
        best_dir = game_map.get_direction_toward(square, find_closest_square(square, enemiesSquares))
            #if best_dir == STILL:
            #    best_dir = random.choice(randomInterCardinalDirection)
            #directionsMatrix[square.x][square.y] = best_dir
        return Move(square, best_dir)

    if len(directions) == 0:
        return Move(square, STILL)

    best_dir = sortedDir.get()
    # Si notre piece n'est pas assez forte, on reste
    if square.strength < game_map.get_target(square, best_dir).strength:
        return Move(square, STILL)

    # Si notre piece est assez forte, on la bouge dans les directions qui ne sont pas encore prises
    return Move(square, best_dir)


while True:
    game_map.get_frame()
    # target = game_map.get_direction_toward_with_A_star(square, game_map.contents[0][0])
    # donne le direction pour aller vers la case 0 a partir du carre donne
    # moves = [Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))) for square in game_map if square.owner == myID]
    enemiesSquares = [return_square(square) for square in game_map if square.owner != myID]
    moves = [assign_move(square, enemiesSquares) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
    currentTurn += 1



# Matrice de direction cardinal
#interCardinalDirectionsMatrix = [[STILL for x in range(heigth)] for y in range(witdh)]

#dim1 = len(interCardinalDirectionsMatrix)
#dim2 = len(interCardinalDirectionsMatrix[0])

#print (str(dim1) + " " + str(dim2))
#print (str(witdh) + " " + str(heigth))

#for j in range(heigth):
#    for i in range(witdh):
#        interCardinalDirectionsMatrix[i][j] = random.choice(interCardinalDirections)

    #
#        squareInterCardinalDirection = interCardinalDirectionsMatrix[square.x][square.y]
#        randomDirection = random.choice(squareInterCardinalDirection)

        # Pousuite de la route vers une direction pour éviter le va et vient
#        return Move(square, randomDirection)