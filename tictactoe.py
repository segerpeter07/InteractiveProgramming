"""
This is a simple tic tac toe game that is meant to be implemented
as a multiplayer game.
I can be modified to play with the computer, however the default is
with another player

@Author: Peter Seger
"""


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
        self.board_vals = {1: 'X', 2: 'D', 3: 'D', 4: 'X', 5: 'D', 6: 'X', 7: 'X', 8: 'D', 9: 'X'}

    def create_board(self):
        print('   |   |')
        print(' ' + self.board_vals[7] + ' | ' + self.board_vals[8] + ' | ' + self.board_vals[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board_vals[4] + ' | ' + self.board_vals[5] + ' | ' + self.board_vals[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board_vals[1] + ' | ' + self.board_vals[2] + ' | ' + self.board_vals[3])
        print('   |   |')


if __name__ == '__main__':
    test = board()
    test.create_board()
