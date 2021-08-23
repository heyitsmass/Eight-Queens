import os 
import time 
import keyboard
from typing import overload 
from chessboard import display
from dataclasses import dataclass 

@dataclass 
class Point: 
    x : int 
    y : int 
    isQueen : bool 
    isSafe  : bool 


board_dimensions = 8
board = []
queens = []

def sortY(e): 
    return e.y

def __init__(init_point): 
    for x in range(board_dimensions): 
        for y in range(board_dimensions): 
            if x is init_point.x and y is init_point.y: 
                board.append(init_point) 
            else: 
                board.append(Point(x, y, False, True))
    board.sort(key=sortY)

def __display__(): 

    print('\n', end = '')
    
    for i in range(len(board)):

        if board[i].isQueen: 
            print('Q', end = ' ')
        elif not board[i].isSafe: 
            print('X', end = ' ')
        else: 
            print('.', end = ' ')
        
        if i < len(board)-1:
            if board[i+1].y > board[i].y:
                print()

    print('\n')

def __locatePoint__(e): 
    try: 
        for i in range(len(board)): 
            if board[i] == e: 
                #print("Located point at index: {0}".format(i)) #Debug
                return i  
    except Exception as e: 
        print("Point not found")

def __markUnsafe__(e): 

    diag_x = e.x + e.y 
    diag_y = e.y - e.x 

    for coord in range(board_dimensions): 
        index_A = __locatePoint__(Point(coord, diag_y, False, True)) 
        index_B = __locatePoint__(Point(diag_x, coord, False, True))
        index_C = __locatePoint__(Point(coord, e.y, False, True))
        index_D = __locatePoint__(Point(e.x, coord, False, True))
        if index_A is not None: board[index_A].isSafe = False
        if index_B is not None: board[index_B].isSafe = False 
        if index_C is not None: board[index_C].isSafe = False 
        if index_D is not None: board[index_D].isSafe = False 
        diag_y += 1
        diag_x -= 1
    
def main(): 

    init_point = Point(4, 5, True, False)

    __init__(init_point)  

    queens.append(init_point) 

    __markUnsafe__(init_point) 

    __display__()


    exit()

main()

