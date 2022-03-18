#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 16:41:56 2022

@author: taylorshaw

This file is a python program to solve the wood calendar puzzle
 game. I'm using a brute force approach, halting when I find an 
 invalid board. The worst case runtime is 46**8. Including all
 orientations, there are 46 pieces- but only 8 actual pieces. The 
 board is 7x7, I've hard coded the board size.'
"""

import copy

class Piece:
    def __init__(self, typ, pieceArray, offset=0):
        
        self.type = typ
        self.pieceArray = pieceArray
        self.offset = offset #in the x direction/ column
        
        
        
    #end class
    # --------------------------
    
#CONSTANTS   
O = "_"
a = "💜"
b = "🧡"
c = "💚"
d = "🛑"
e = "💙"
f = "🤎"
g = "💛"
h = "🤍"
    
#the 2x3 rectangle
pieceA0 = Piece(a,[[a, a, a], [a, a, a]])
pieceA1 = Piece(a, [[a, a], [a, a], [a, a]])

#the symetrical dorner
pieceB0 = Piece(b, [[b, b, b], [b, O, O], [b, O, O]])
pieceB1 = Piece(b, [[b, O, O], [b, O, O], [b, b, b]])
pieceB2 = Piece((b), [[b, b, b], [O, O, b], [O, O, b]])
pieceB3 = Piece(b, [[O, O, b], [O, O, b], [b, b, b]], 2)

#the C piece
pieceC0 = Piece(c, [[c, c, c], [c, O, c]])
pieceC1 = Piece(c, [[c, c], [c, O], [c, c]])
pieceC2 = Piece(c, [[c, c], [O, c], [c, c]])
pieceC3 = Piece(c, [[c, O, c], [c, c, c]])

#the T piece
pieceD0 = Piece(d, [[d, d, d], [O, d, O], [O, d, O]])
pieceD1 = Piece(d,[[d, O, O], [d, d, d], [d, O, O]])
pieceD2 = Piece(d, [[O, O, d], [d, d, d], [O, O, d]], 2)
pieceD3 = Piece(d, [[O, d, O], [O, d, O], [d, d, d]], 1)
           
#asymetrical corner or L
pieceE0 = Piece(e, [[e, O, O, O], [e, e, e, e]])
pieceE1 = Piece(e, [[O, O, O, e], [e, e, e, e]], 3)
pieceE2 = Piece(e, [[O, e], [O, e], [O, e], [e, e]], 1)
pieceE3 = Piece(e, [[e, O], [e, O], [e, O], [e, e]])
pieceE4 = Piece(e, [[e, e], [O, e], [O, e], [O, e]])
pieceE5 = Piece(e, [[e, e], [e, O], [e, O], [e, O]])
pieceE6 = Piece(e, [[e, e, e, e], [O, O, O, e]])
pieceE7 = Piece(e, [[e, e, e, e], [e, O, O, O]])

#asymetrical zig zag
pieceF0 = Piece(f, [[f, O], [f, O], [f, f], [O, f]])
pieceF1 = Piece(f, [[O, f], [O, f], [f, f], [f, O]], 1)
pieceF2 = Piece(f, [[f, O], [f, f], [O, f], [O, f]])
pieceF3 = Piece(f, [[O, f], [f, f], [f, O], [f, O]], 1)
pieceF4 = Piece(f, [[f, f, O, O], [O, f, f, f]])
pieceF5 = Piece(f, [[O, f, f, f], [f, f, O, O]], 1)
pieceF6 = Piece(f, [[O, O, f, f], [f, f, f, O]], 2)
pieceF7 = Piece(f, [[f, f, f, O], [O, O, f, f]])

# 2x3 rectangle - 1 corner
pieceG0 = Piece(g, [[O, g, g], [g, g, g]], 1)
pieceG1 = Piece(g, [[g, g, g], [O, g, g]])
pieceG2 = Piece(g, [[g, g, O], [g, g, g]])
pieceG3 = Piece(g, [[g, g, g], [g, g, O]])
pieceG4 = Piece(g, [[g, g], [g, g], [O, g]])
pieceG5 = Piece(g, [[g, g], [g, g], [g, O]])
pieceG6 = Piece(g, [[g, O], [g, g], [g, g]])
pieceG7 = Piece(g, [[O, g], [g, g], [g, g]], 1)

#line with 1 nub
pieceH0 = Piece(h, [[O, O, h, O], [h, h, h, h]], 2)
pieceH1 = Piece(h, [[O, h, O, O], [h, h, h, h]], 1)
pieceH2 = Piece(h, [[h, h, h, h], [O, O, h, O]])
pieceH3 = Piece(h, [[h, h, h, h], [O, h, O, O]])
pieceH4 = Piece(h, [[O, h], [h, h], [O, h], [O, h]], 1)
pieceH5 = Piece(h, [[O, h], [O, h], [h, h], [O, h]], 1)
pieceH6 = Piece(h, [[h, O], [h, h], [h, O], [h, O]])
pieceH7 = Piece(h, [[h, O], [h, O], [h, h], [h, O]])


allPieces = [pieceA0, pieceA1, pieceB0, pieceB1, pieceB2, pieceB3, pieceC0, 
             pieceC1, pieceC2, pieceC3, pieceD0, pieceD1, pieceD2, pieceD3,
             pieceE0, pieceE1, pieceE2, pieceE3, pieceE4, pieceE5, pieceE6,
             pieceE7, pieceF0, pieceF1, pieceF2, pieceF3, pieceF4, pieceF5,
             pieceF6, pieceF7, pieceG0, pieceG1, pieceG2, pieceG3, pieceG4,
             pieceG5, pieceG6, pieceG7, pieceH0, pieceH1, pieceH2, pieceH3,
             pieceH4, pieceH5, pieceH6, pieceH7]




# print(len(allPieces))


board = [["_", "_", "M", "_", "_", "_", "X"], #JAN-JUN
         ["_", "_", "_", "_", "_", "_", "X"], #JUL-DEC
         ["_", "_", "_", "_", "_", "_", "_"], #1-7
         ["_", "_", "_", "_", "0", "_", "_"], #8-14
         ["_", "_", "_", "_", "_", "_", "_"], #15-21
         ["_", "_", "_", "_", "_", "_", "_"], #22-28
         ["_", "_", "_", "X", "X", "X", "X"]] #29-31

# JAN = [0][0]
# FEB = [0][1]
# MAR = [0][2]
# APR = [0][3]
# MAY = [0][4]
# JUN = [0][5]

# board[0][1] = "0"

def printBoard(board):
    if board is None:
        print(board)
        return
    for row in board:
        print(row)
  


#-----------------------------                
                
def solve(allPieces, board, recurDepth=0):
    """

    Parameters
    ----------
    allPieces : [Piece]
        DESCRIPTION. all remaining pieces that can be placed on the board
    board : [[]]
        DESCRIPTION. 2D array representing the board

    Returns
    -------
    a valid solution, or None if none exists

    """
    # print("recurDepth:", recurDepth)
    for p in allPieces:
        tempBoard = placePieceOnBoard(board, p)
        if tempBoard is not None:
            won = findFirstEmptySpace(tempBoard)
            if won == None:
                return tempBoard
            else: #haven't won
                
                remainingPiecesIter = filter(lambda piece: piece.type != p.type, allPieces)
                
                answer = solve(list(remainingPiecesIter), tempBoard, recurDepth+1)
                if answer == None:
                    continue
                else:
                    return answer
        # else, tempBoard is None
        
    #end for
    return None
       
       
def findFirstEmptySpace(board):
    """
    

    Parameters
    ----------
    board : [[]]
        DESCRIPTION. 2D board array

    Returns
    -------
    (r, c) representing the row and column of the first '_' space
    else None
no empty space means you won
    """
    #board is 7x7
    for r in range(7):
        for c in range(7):
            if board[r][c] == "_":
                return (r, c)
    return None 



def placePieceOnBoard(board, piece):
    """
    
    Parameters
    ----------
    board : [[]]
        DESCRIPTION. 2D array, represents state of board before adding piece
    piece : Piece object
        DESCRIPTION. Piece to be placed on board

    Returns
    -------
    new board array with valid placement of piece on board, else None.
    It's considered a valid placement if the piece is fully
    on the board and not covering occupied squares

    """
    #get dims of piece, every piece is a rectangle
    pWidth = len(piece.pieceArray[0])
    pHeight = len(piece.pieceArray)
    off = piece.offset
   
    
    # find first empty space
    (r, c) = findFirstEmptySpace(board)
    #check dims, board dims are 7x7
    if pWidth+c-off <= 7 and pHeight+r <= 7 and c-off >= 0:
        
        # place piece, write new board
        newBoard = copy.deepcopy(board)
        for col in range(pWidth):
            for row in range (pHeight):
                
                #if board is blank
                if newBoard[r+row][c+col-off] == "_":
                    newBoard[r+row][c+col-off] = piece.pieceArray[row][col]
                    
                #if board is not blank but piece is blank
                elif piece.pieceArray[row][col] == "_":
                    continue
                else:
                    #exiting with collision
                    return None
        #end for
        return newBoard
    #wrong dimensions
    return None
        

    

    
# print("board:")  
# printBoard(board)
 
# other = copy.deepcopy(board)
# other[0][1] = "c"
# other[0][0] = "b"
# other[0][2] = "d"
# other[0][4] = "d"
# other[0][3] = "d"
# other[0][5] = "e"


#TEST findFirstEmptySpace()

# print("other:")
# printBoard(other)
# out = findFirstEmptySpace(other)
# print(out)

#TEST placePieceOnBoard
# new = placePieceOnBoard(other, pieceA0)
# print("board:")
# printBoard(board)
# print("other:")
# printBoard(other)
# print("new:")
# # print(new)
# # printBoard(new)
# print("pieceA0")
# printBoard(pieceA0.pieceArray)


# newBoard = [["_", "_", "_", "0", "0", "0", "X"], #JAN-JUN
#          ["_", "_", "_", "0", "0", "0", "X"], #JUL-DEC
#          ["3", "3", "3", "3", "3", "0", "0"], #1-7
#          ["3", "3", "3", "0", "0", "3", "0"], #8-14
#          ["3", "3", "3", "0", "0", "3", "0"], #15-21
#          ["4", "0", "4", "0", "4", "4", "4"], #22-28
#          ["5", "5", "5", "X", "X", "X", "X"]] #29-31

# solution = [["b", "b", "b", "0", "0", "0", "X"], #JAN-JUN
#          ["b", "e", "0", "0", "0", "0", "X"], #JUL-DEC
#          ["b", "e", "e", "e", "e", "0", "0"], #1-7
#          ["a", "a", "a", "0", "0", "d", "0"], #8-14
#          ["a", "a", "a", "0", "0", "d", "0"], #15-21
#          ["c", "0", "c", "0", "d", "d", "d"], #22-28
#          ["c", "c", "c", "X", "X", "X", "X"]] #29-31

# test = solve(allPieces, newBoard, 0)
# print("first empty")
# print(findFirstEmptySpace(test))
# print("result of solve")
# printBoard(test)
# print("end result")
#TEST pieces, filter
# for p in allPieces:
#     printBoard(p.pieceArray)

# print("filtered")

# left = list(filter(lambda piece: piece.type != "b", allPieces))

# for p in left:
#     printBoard(p.pieceArray)

# printBoard(pieceC0.pieceArray)

# testBoard = [["_", "_", "_", "0", "0", "0", "X"], #JAN-JUN
#          ["_", "_", "0", "0", "0", "0", "X"], #JUL-DEC
#          ["_", "_", "_", "_", "_", "0", "0"], #1-7
#          ["_", "_", "_", "0", "0", "_", "0"], #8-14
#          ["_", "_", "_", "0", "0", "_", "0"], #15-21
#          ["_", "0", "_", "0", "_", "_", "_"], #22-28
#          ["_", "_", "_", "X", "X", "X", "X"]] #29-31

# solution = [["b", "b", "b", "0", "0", "0", "X"], #JAN-JUN
#          ["b", "e", "0", "0", "0", "0", "X"], #JUL-DEC
#          ["b", "e", "e", "e", "e", "0", "0"], #1-7
#          ["a", "a", "a", "0", "0", "d", "0"], #8-14
#          ["a", "a", "a", "0", "0", "d", "0"], #15-21
#          ["c", "0", "c", "0", "d", "d", "d"], #22-28
#          ["c", "c", "c", "X", "X", "X", "X"]] #29-31
new = solve(allPieces, board)
# printBoard(new)
print("Result of solve:")
printBoard(new)
print("* end result *")






