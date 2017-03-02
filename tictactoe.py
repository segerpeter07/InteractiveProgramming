"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
I can be modified to play with the computer, however the default is
with another player

@Author: Peter Seger
"""

from numpy import *

class board():
    """
    This is the game board which contains functions to:
    -Create the board
    -Update the board
    -Print the board
    -Add a play piece
    -Clear the board
    """

    def __init__(self):
        rows, collumns = 11, 11
        self.matrix = [[0 for x in range(collumns)] for y in range(rows)]
        self.board_vals = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

    def create_board(self):
        rows, collumns = 11, 11
        """Manually filling in the matrix with board indexes"""
        self.matrix[2][2] = self.board_vals[1]
        self.matrix[2][6] = self.board_vals[2]
        self.matrix[2][10] = self.board_vals[3]

        self.matrix[6][2] = self.board_vals[4]
        self.matrix[6][6] = self.board_vals[5]
        self.matrix[6][10] = self.board_vals[6]

        self.matrix[10][2] = self.board_vals[7]
        self.matrix[10][6] = self.board_vals[8]
        self.matrix[10][10] = self.board_vals[9]

        """Fill board with boarders and dividers"""
        for i in range(collumns):
            self.matrix[4][i] = '-'
            self.matrix[8][i] = '-'
        for j in range(rows):
            self.matrix[j][4] = '|'
            self.matrix[j][8] = '|'

    # def update_board(self, location, choice):

    def __str__(self):
        res = array([self.matrix[1],
                        self.matrix[2],
                        self.matrix[3],
                        self.matrix[4],
                        self.matrix[5],
                        self.matrix[6],
                        self.matrix[7],
                        self.matrix[8],
                        self.matrix[9],
                        self.matrix[10],
                        ])
        return(str(res))


if __name__ == '__main__':
    test = board()
    test.create_board()
    print(test)
