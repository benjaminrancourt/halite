import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random


myID, game_map = hlt.get_init()
hlt.send_init("TofuBot")

while True:
    game_map.get_frame()
    # target = game_map.get_direction_toward_with_A_star(square, game_map.contents[0][0])
    # donne le direction pour aller vers la case 0 a partir du carre donne
    moves = [Move(square, random.choice((NORTH, EAST, SOUTH, WEST, STILL))) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
